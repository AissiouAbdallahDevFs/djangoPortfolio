import './StyleIntroductionBubble.css';
import ExperienceBubble from "../experiences/ExperienceBubble"
import DiplomeBubble from "../diplomes/DiplomesBubble"
import ContactForm from "../messages/MessageBubble"
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';


const baseUrl = 'https://nabdou.pythonanywhere.com';

const Skill = ({ skill }) => (
  <div key={skill.id} className="skill">
    <img className="w-12" src={`${baseUrl}${skill.skillsImage}`} alt={skill.skillsName} />
  </div>
);

const SkillsSlider = ({ skills }) => {
  const sliderSettings = {
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    speed: 2000,
    autoplaySpeed: 2000,
    pauseOnHover: true,
    responsive: [
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  };

  return (
    <Slider {...sliderSettings}>
      {skills.map((skill) => (
        <Skill skill={skill} />
      ))}
    </Slider>
  );
};

const IntroductionBubble = () => {
  const [aboutData, setAboutData] = useState(null);

  useEffect(() => {
    axios
      .get(`${baseUrl}/src/about/`)
      .then((response) => {
        if (response.status === 200) {
          const about = response.data[0];
          setAboutData(about);
          console.log('Données d\'expérience récupérées avec succès !🧑🏽‍💻🧑🏽‍💻🧑🏽‍💻🧑🏽‍💻');
        }
      })
      .catch((error) => {
        console.error('Une erreur s\'est produite lors de la récupération des données d\'expérience :', error);
      });
  }, []);

  return (
    <div className="bg-gray-200 min-h-screen flex items-center justify-center p-5">
      <div className="bg-white p-6 rounded-lg shadow-md w-9/12">
        <img
          className="profile-image rounded-full mx-auto mb-4 w-32"
          src={`${baseUrl}${aboutData ? aboutData.aboutImage : 'Chargement...'}`}
          alt={aboutData ? aboutData.aboutTitle : 'Chargement...'}
        />
        <h1 className="text-2xl font-bold mb-2">
          {aboutData ? aboutData.aboutTitle : 'Chargement...'}
        </h1>
        <div className="text-gray-600">
          <h1 className="text-lg font-bold mb-2">À propos de moi</h1>
          <p className="mb-8 p-5">
            {aboutData ? aboutData.aboutDescription : 'Chargement...'}
          </p>
        </div>
        <h1 className="text-2xl font-bold mb-2">Skills</h1>
        {aboutData && aboutData.skills && <SkillsSlider skills={aboutData.skills} />}
        <h1 className="text-2xl font-bold mb-2">Experiences</h1>
        <ExperienceBubble />
        <h2 className="text-2xl font-bold mb-2">Diplomes</h2>
        <DiplomeBubble />
        <ContactForm />
      </div>
    </div>
  );
};

export default IntroductionBubble;
