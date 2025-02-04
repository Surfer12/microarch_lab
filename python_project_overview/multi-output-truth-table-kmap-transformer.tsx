import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const MultiOutputTruthTableKMapTransformer = () => {
  // Initial truth table state with 3-bit inputs and 3-bit outputs
  const [truthTable, setTruthTable] = useState([
    { x2: 0, x1: 0, x0: 0, y2: 1, y1: 0, y0: 1 },
    { x2: 0, x1: 0, x0: 1, y2: 0, y1: 1, y0: 0 },
    { x2: 0, x1: 1, x0: 0, y2: 0, y1: 0, y0: 0 },
    { x2: 0, x1: 1, x0: 1, y2: 1, y1: 1, y0: 1 },
    { x2: 1, x1: 0, x0: 0, y2: 1, y1: 0, y0: 1 },
    { x2: 1, x1: 0, x0: 1, y2: 0, y1: 1, y0: 0 },
    { x2: 1, x1: 1, x0: 0, y2: 1, y1: 0, y0: 1 },
    { x2: 1, x1: 1, x0: 1, y2: 0, y1: 1, y0: 0 }
  ]);

  // Gray code sequence for columns
  const grayCodeColumns = ['00', '01', '11', '10'];

  // Toggle output in truth table
  const toggleOutput = (index, outputColumn) => {
    const newTruthTable = [...truthTable];
    newTruthTable[index][outputColumn] = newTruthTable[index][outputColumn] === 1 ? 0 : 1;
    setTruthTable(newTruthTable);
  };

  // Generate K-Maps from truth table
  const generateKMaps = () => {
    const outputColumns = ['y2', 'y1', 'y0'];
    
    return outputColumns.reduce((acc, outputColumn) => {
      const kMap = {
        x2_0: [0, 0, 0, 0],
        x2_1: [0, 0, 0, 0]
      };

      truthTable.forEach(row => {
        const rowIndex = row.x2;
        const colIndex = grayCodeColumns.indexOf(`${row.x1}${row.x0}`);
        
        kMap[`x2_${rowIndex}`][colIndex] = row[outputColumn];
      });

      acc[outputColumn] = kMap;
      return acc;
    }, {});
  };

  const kMaps = generateKMaps();

  // Color coding function
  const getOutputColor = (output) => 
    output === 1 ? 'bg-green-200' : 'bg-red-200';

  return (
    <Card className="w-full max-w-5xl">
      <CardHeader>
        <CardTitle>Multi-Output Truth Table to K-Map Transformer</CardTitle>
      </CardHeader>
      <CardContent className="grid grid-cols-3 gap-4">
        {/* Truth Table Section */}
        <div className="col-span-1 border rounded p-4">
          <h3 className="text-lg font-bold mb-4">Truth Table</h3>
          <table className="w-full text-sm">
            <thead>
              <tr>
                <th>X2</th>
                <th>X1</th>
                <th>X0</th>
                <th>Y2</th>
                <th>Y1</th>
                <th>Y0</th>
              </tr>
            </thead>
            <tbody>
              {truthTable.map((row, index) => (
                <tr key={index} className="hover:bg-gray-100">
                  <td className="text-center">{row.x2}</td>
                  <td className="text-center">{row.x1}</td>
                  <td className="text-center">{row.x0}</td>
                  {['y2', 'y1', 'y0'].map(outputColumn => (
                    <td 
                      key={outputColumn}
                      className={`text-center cursor-pointer ${getOutputColor(row[outputColumn])}`}
                      onClick={() => toggleOutput(index, outputColumn)}
                    >
                      {row[outputColumn]}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* K-Map Sections for Y2, Y1, Y0 */}
        {['y2', 'y1', 'y0'].map(outputColumn => (
          <div key={outputColumn} className="border rounded p-4">
            <h3 className="text-lg font-bold mb-4">K-Map for {outputColumn.toUpperCase()} (Gray Code)</h3>
            <div className="grid grid-cols-5 gap-2">
              <div className="col-span-1"></div>
              {grayCodeColumns.map(col => (
                <div key={col} className="text-center font-bold">{col}</div>
              ))}
              
              {[0, 1].map(x2 => (
                <React.Fragment key={`row-${x2}`}>
                  <div className="text-center font-bold">X2 = {x2}</div>
                  {grayCodeColumns.map((col, index) => (
                    <div 
                      key={`cell-${x2}-${col}`} 
                      className={`
                        border h-16 flex items-center justify-center
                        ${getOutputColor(kMaps[outputColumn][`x2_${x2}`][index])}
                      `}
                    >
                      {kMaps[outputColumn][`x2_${x2}`][index]}
                    </div>
                  ))}
                </React.Fragment>
              ))}
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
};

export default MultiOutputTruthTableKMapTransformer;
