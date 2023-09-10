import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ExperienceBubble = () => {
  const [experienceData, setExperienceData] = useState(null);
  const baseUrl = 'http://127.0.0.1:8000';

  useEffect(() => {
    axios.get(`${baseUrl}/src/experience/`)
      .then(response => {
        if (response.status === 200) {
          const experience = response.data[0];
          setExperienceData(experience);
          console.log('Données d\'expérience récupérées avec succès !🧑🏽‍💻🧑🏽‍💻🧑🏽‍💻🧑🏽‍💻');
        }
      })
      .catch(error => {
        console.error('Une erreur s\'est produite lors de la récupération des données d\'expérience :', error);
      });
  }, []);

  return (
    <div className="experience-bubble p-4 sm:p-12">
      {experienceData && (
        <div className="bg-white dark:bg-gray-800 shadow-md rounded-lg overflow-hidden mx-auto max-w-sm">
          <img className="w-full h-48 sm:h-16 object-cover object-center" src={`${baseUrl}${experienceData.experienceImage}`} alt={experienceData.experienceName} />
          <div className="p-4">
            <h2 className="text-xl sm:text-2xl font-semibold text-gray-800 dark:text-white mb-2">{experienceData.experienceName}</h2>
            <p className="text-gray-600 dark:text-gray-400">{experienceData.experienceDescription}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExperienceBubble;

