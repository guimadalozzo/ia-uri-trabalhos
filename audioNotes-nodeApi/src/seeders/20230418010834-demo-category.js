'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
    await queryInterface.bulkInsert('Categories', [
    {
      name: 'Ideia',
      createdAt: new Date(),
      updatedAt: new Date()
    },
    {
      name: 'Estudo',
      createdAt: new Date(),
      updatedAt: new Date()
    },
    {
      name: 'Casa',
      createdAt: new Date(),
      updatedAt: new Date()
    },
    {
      name: 'Trabalho',
      createdAt: new Date(),
      updatedAt: new Date()
    },
  ], {});
  },

  async down (queryInterface, Sequelize) {
    await queryInterface.bulkDelete('Categories', null, {});
  }
};
