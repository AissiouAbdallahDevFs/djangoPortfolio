import React, { useState } from 'react';
import axios from 'axios';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    emailUser: '',
    messageUser: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post('https://nabdou.pythonanywhere.com/src/messages/add', formData)
      .then((response) => {
          toast.success('Message envoyé avec succès !',  {
            position: 'top-right',
            autoClose: 3000,
            hideProgressBar: false,
            closeOnClick: true,
            pauseOnHover: true,
            draggable: true,
          });

          setFormData({ emailUser: '', messageUser: '' });
        }
        )
      .catch((error) => {
        console.error("Une erreur s'est produite lors de l'envoi du message :", error);
      });
  };

  return (
    <div className="contact-form bg-gray-100 p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-semibold mb-4">Contactez-Moi</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label htmlFor="emailUser" className="block text-gray-600">Email :</label>
          <input
            type="email"
            id="emailUser"
            name="emailUser"
            value={formData.emailUser}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500"
          />
        </div>
        <div className="mb-4">
          <label htmlFor="messageUser" className="block text-gray-600">Message :</label>
          <textarea
            id="messageUser"
            name="messageUser"
            value={formData.messageUser}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500 resize-none"
            rows="4"
          />
        </div>
        <button
          type="submit"
          className="bg-gray-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition duration-300"
        >
          Envoyer
        </button>
      </form>
      <ToastContainer />
    </div>
  );
};

export default ContactForm;

