import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DiplomeBubble = () => {
  const [diplomeData, setDiplomeData] = useState([]);
  const baseUrl = 'http://127.0.0.1:8000';

  useEffect(() => {
    axios.get(`${baseUrl}/src/degrees/`)
      .then(response => {
        if (response.status === 200) {
          const diplomes = response.data;
          setDiplomeData(diplomes);
          console.log('Données des diplômes récupérées avec succès !🧑🏽‍💻🧑🏽‍💻🧑🏽‍💻🧑🏽‍💻');
        }
      })
      .catch(error => {
        console.error('Une erreur s\'est produite lors de la récupération des données des diplômes :', error);
      });
  }, []);

  let gridColumns = 'grid-cols-1';

  if (diplomeData.length === 2) {
    gridColumns = 'sm:grid-cols-2';
  } else if (diplomeData.length === 1) {
    gridColumns = 'sm:grid-cols-1';
  } else {
    gridColumns = 'md:grid-cols-3';
  }

  return (
    <div className={`diplome-bubble p-4 sm:p-12 grid ${gridColumns} gap-4 justify-center`}>
      {diplomeData.map((diplome, index) => (
        <div key={index} className="bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-hidden mx-auto max-w-sm flex flex-col">
          <img className="w-full h-48 sm:h-16 object-cover object-center" src={`${baseUrl}${diplome.degreesImage}`} alt={diplome.degreesName} />
          <div className="p-4 flex-grow">
            <h2 className="text-xl sm:text-2xl font-semibold text-gray-800 dark:text-white mb-2">{diplome.degreesName}</h2>
            <p className="text-gray-600 dark:text-gray-400">{diplome.degreesDescription}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default DiplomeBubble;


