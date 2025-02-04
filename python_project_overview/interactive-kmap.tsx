import React, { useState } from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';

const KMapInteractive = () => {
  const [selectedCells, setSelectedCells] = useState(new Set());

  const grayCodeColumns = ['00', '01', '11', '10'];
  const rows = [0, 1];  // X2 values

  const handleCellClick = (row, colIndex) => {
    const cellKey = `${row}-${colIndex}`;
    setSelectedCells(prev => {
      const newSet = new Set(prev);
      newSet.has(cellKey) ? newSet.delete(cellKey) : newSet.add(cellKey);
      return newSet;
    });
  };

  return (
    <Card className="w-full max-w-2xl p-4">
      <CardHeader>
        <CardTitle>Interactive K-Map Reasoning Visualization</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-5 gap-2">
          <div className="col-span-1 text-center font-bold">X2 \ X1X0</div>
          {grayCodeColumns.map((col, index) => (
            <div key={col} className="text-center font-bold">{col}</div>
          ))}
          
          {rows.map(row => (
            <>
              <div key={`row-${row}`} className="text-center font-bold">{row}</div>
              {grayCodeColumns.map((col, colIndex) => (
                <div 
                  key={`${row}-${colIndex}`}
                  onClick={() => handleCellClick(row, colIndex)}
                  className={`
                    border-2 h-16 flex items-center justify-center cursor-pointer
                    ${selectedCells.has(`${row}-${colIndex}`) 
                      ? 'bg-blue-200 border-blue-500' 
                      : 'bg-gray-100 border-gray-300'}
                  `}
                >
                  {selectedCells.has(`${row}-${colIndex}`) ? '1' : '0'}
                </div>
              ))}
            </>
          ))}
        </div>
        <div className="mt-4 text-sm text-gray-600">
          Click cells to toggle logical states. Explore adjacency and grouping patterns.
        </div>
      </CardContent>
    </Card>
  );
};

export default KMapInteractive;
