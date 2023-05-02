'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Conversation extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      Conversation.belongsTo(models.Category, {
        foreignKey: 'category_id'
      })
      Conversation.belongsTo(models.User, {
        foreignKey: 'user_id'
      })
      Conversation.hasMany(models.Message, {
        foreignKey: 'conversation_id'
      })
    }
  }
  Conversation.init({
    name: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'Conversation',
  });
  return Conversation;
};