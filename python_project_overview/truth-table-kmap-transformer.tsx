import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const TruthTableKMapTransformer = () => {
  // Initial truth table state with 3-bit inputs
  const [truthTable, setTruthTable] = useState([
    { x2: 0, x1: 0, x0: 0, output: 1 },
    { x2: 0, x1: 0, x0: 1, output: 0 },
    { x2: 0, x1: 1, x0: 0, output: 0 },
    { x2: 0, x1: 1, x0: 1, output: 1 },
    { x2: 1, x1: 0, x0: 0, output: 1 },
    { x2: 1, x1: 0, x0: 1, output: 0 },
    { x2: 1, x1: 1, x0: 0, output: 1 },
    { x2: 1, x1: 1, x0: 1, output: 0 }
  ]);

  // Gray code sequence for columns
  const grayCodeColumns = ['00', '01', '11', '10'];

  // Toggle output in truth table
  const toggleOutput = (index) => {
    const newTruthTable = [...truthTable];
    newTruthTable[index].output = newTruthTable[index].output === 1 ? 0 : 1;
    setTruthTable(newTruthTable);
  };

  // Generate K-Map from truth table
  const generateKMap = () => {
    const kMap = {
      x2_0: [0, 0, 0, 0],
      x2_1: [0, 0, 0, 0]
    };

    truthTable.forEach(row => {
      const rowIndex = row.x2;
      const colIndex = grayCodeColumns.indexOf(`${row.x1}${row.x0}`);
      
      kMap[`x2_${rowIndex}`][colIndex] = row.output;
    });

    return kMap;
  };

  const kMap = generateKMap();

  return (
    <Card className="w-full max-w-4xl">
      <CardHeader>
        <CardTitle>Truth Table to K-Map Transformer</CardTitle>
      </CardHeader>
      <CardContent className="grid grid-cols-2 gap-4">
        {/* Truth Table Section */}
        <div className="border rounded p-4">
          <h3 className="text-lg font-bold mb-4">Truth Table</h3>
          <table className="w-full">
            <thead>
              <tr>
                <th>X2</th>
                <th>X1</th>
                <th>X0</th>
                <th>Output</th>
              </tr>
            </thead>
            <tbody>
              {truthTable.map((row, index) => (
                <tr key={index} 
                    className="hover:bg-gray-100 cursor-pointer"
                    onClick={() => toggleOutput(index)}
                >
                  <td className="text-center">{row.x2}</td>
                  <td className="text-center">{row.x1}</td>
                  <td className="text-center">{row.x0}</td>
                  <td 
                    className={`text-center ${row.output ? 'bg-green-200' : 'bg-red-200'}`}
                  >
                    {row.output}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* K-Map Section */}
        <div className="border rounded p-4">
          <h3 className="text-lg font-bold mb-4">K-Map (Gray Code)</h3>
          <div className="grid grid-cols-5 gap-2">
            <div className="col-span-1"></div>
            {grayCodeColumns.map(col => (
              <div key={col} className="text-center font-bold">{col}</div>
            ))}
            
            {[0, 1].map(x2 => (
              <>
                <div key={`row-label-${x2}`} className="text-center font-bold">X2 = {x2}</div>
                {grayCodeColumns.map((col, index) => (
                  <div 
                    key={`cell-${x2}-${col}`} 
                    className={`
                      border h-16 flex items-center justify-center
                      ${kMap[`x2_${x2}`][index] ? 'bg-green-200' : 'bg-red-200'}
                    `}
                  >
                    {kMap[`x2_${x2}`][index]}
                  </div>
                ))}
              </>
            ))}
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default TruthTableKMapTransformer;
