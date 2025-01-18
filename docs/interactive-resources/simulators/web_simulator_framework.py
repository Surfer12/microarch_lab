import flask
import json
from typing import Dict, Any

class HardwareSimulationFramework:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.simulators = {}
    
    def register_simulator(self, name: str, simulator_class):
        """
        Register a new hardware simulator
        
        Args:
            name (str): Unique identifier for the simulator
            simulator_class (type): Simulator class to register
        """
        self.simulators[name] = simulator_class()
    
    def create_simulation_routes(self):
        """
        Create Flask routes for each registered simulator
        """
        @self.app.route('/simulate/<simulator_name>', methods=['POST'])
        def simulate(simulator_name):
            if simulator_name not in self.simulators:
                return flask.jsonify({
                    'error': f'Simulator {simulator_name} not found'
                }), 404
            
            try:
                input_data = flask.request.json
                simulator = self.simulators[simulator_name]
                result = simulator.simulate(input_data)
                return flask.jsonify(result)
            except Exception as e:
                return flask.jsonify({
                    'error': str(e)
                }), 500
    
    def run(self, debug=True, port=5000):
        """
        Run the simulation framework
        
        Args:
            debug (bool): Enable debug mode
            port (int): Port to run the server
        """
        self.create_simulation_routes()
        self.app.run(debug=debug, port=port)

class CPUSimulator:
    def simulate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate CPU operations
        
        Args:
            input_data (dict): Simulation configuration
        
        Returns:
            dict: Simulation results
        """
        registers = input_data.get('registers', [0] * 8)
        instructions = input_data.get('instructions', [])
        
        # Simulate instruction execution
        for instruction in instructions:
            op = instruction[0]
            if op == 'LOAD':
                registers[instruction[1]] = instruction[2]
            elif op == 'ADD':
                registers[instruction[1]] = (
                    registers[instruction[2]] + 
                    registers[instruction[3]]
                )
        
        return {
            'final_registers': registers,
            'instruction_count': len(instructions)
        }

class MemoryHierarchySimulator:
    def simulate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulate memory hierarchy performance
        
        Args:
            input_data (dict): Simulation configuration
        
        Returns:
            dict: Simulation results
        """
        cache_levels = input_data.get('cache_levels', 3)
        memory_access_pattern = input_data.get('memory_access_pattern', [])
        
        cache_hits = [0] * cache_levels
        cache_misses = [0] * cache_levels
        
        for address in memory_access_pattern:
            # Simulate cache lookup
            hit_level = self._simulate_cache_lookup(address, cache_levels)
            if hit_level is not None:
                cache_hits[hit_level] += 1
            else:
                cache_misses[-1] += 1
        
        return {
            'cache_hits': cache_hits,
            'cache_misses': cache_misses,
            'hit_rates': [
                hits / (hits + misses) if (hits + misses) > 0 else 0
                for hits, misses in zip(cache_hits, cache_misses)
            ]
        }
    
    def _simulate_cache_lookup(self, address, cache_levels):
        # Simplified cache lookup simulation
        # In a real implementation, this would use more complex cache modeling
        return None if len(address) % cache_levels == 0 else 0

def main():
    # Create simulation framework
    sim_framework = HardwareSimulationFramework()
    
    # Register simulators
    sim_framework.register_simulator('cpu', CPUSimulator)
    sim_framework.register_simulator('memory_hierarchy', MemoryHierarchySimulator)
    
    # Run the framework
    sim_framework.run()

if __name__ == '__main__':
    main() 