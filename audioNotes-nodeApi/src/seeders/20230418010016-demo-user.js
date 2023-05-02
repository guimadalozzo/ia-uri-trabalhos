'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Users', [
    {
      firstName: 'Igor',
      lastName: 'Follador',
      phone: '54996711882',
      email: 'igorledf@hotmail.com',
      password: '$2b$10$nOo.utPUk5uPC0L4GKrJXOI1Cw9sgpQKKxQARxm31YJXSms2xFLW6',
      createdAt: new Date(),
      updatedAt: new Date()
    },
    {
      firstName: 'Jaisson',
      lastName: 'Bassanesi',
      phone: '54992026787',
      email: 'jaisson@bassanesi.com',
      password: '$2b$10$DYfI9JhEdhZxFXpmq5CBVOn1SMZn9bEwE8xCZIg/yYQvz.vThX03u',
      createdAt: new Date(),
      updatedAt: new Date()
    },
  ], {});
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Users', null, {});
  }
};
