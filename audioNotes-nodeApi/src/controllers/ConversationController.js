const database = require('../models');
const service = require('../services/ConversationService');
const dates = require('../services/Dates');

class ConversationController {
    
    static async storageMessage(req, res) {
        try {
            const dataForm = req.body;
            const userId = req.userId;
            let conversation;
            
            if (!dataForm.conversation_id || dataForm.conversation_id == null) {
                const categoryAlias = service.verifyCategory(dataForm.content);
                const conversationName = service.createNameByText(dataForm.content);
                const conversationForm = service.createConversationForm(conversationName, categoryAlias, userId);

                conversation = await database.Conversation.create(conversationForm);
            } else {
                conversation = await database.Conversation.findOne({ where: {
                    id: dataForm.conversation_id,
                    user_id: userId
                } });
            }

            const category = await database.Category.findOne({ where: { id: conversation.category_id } });
            const message = await database.Message.create(service.createMessageForm(dataForm.content, conversation.id));
            const messageDate = dates.formatToDMY(message.createdAt.toISOString().split('T')[0]);
            const time = message.createdAt.toISOString().split('T')[1];
            const messageTime = (time.split(':')[0] - 3)+ ":" + time.split(':')[1];

            const responseData = {
                conversation_id: conversation.id,
                conversation_name: conversation.name,
                category_name: category.name,
                message_id: message.id,
                message_content: message.content,
                message_date: messageDate,
                message_time: messageTime
            }
           
            return res.status(201).send(responseData);

        } catch (error) {
            return res.status(500).send({ message: error.message });
        }
    }

    static async readAll(req, res) {
        try {
            const userId = req.userId;

            const conversations = await database.Conversation.findAll({ 
                include: {
                    model: database.Category,
                    attributes: ['id', 'name']
                },
                attributes: ['id','name'],
                where: { user_id: userId },
                order: [['createdAt', 'DESC']]
            });

            let allConversations = [];

            conversations.forEach(conversation => {
                let conversationData = {};
            
                conversationData.conversation_id = conversation.id;
                conversationData.conversation_name = conversation.name;
                conversationData.category_name = conversation.Category.name;
                
                allConversations.push(conversationData);
            });

            return res.status(200).send(allConversations);
        } catch (error) {
            return res.status(500).send({ message: error.message })
        }
    }

    static async readConversation(req, res) {
        try {
            const { id } = req.params;

            const conversation = await database.Conversation.findOne({ 
                include: {
                    model: database.Category,
                    attributes: ['id', 'name']
                },
                attributes: ['id','name'],
                where: { id: id }
            });

            const messages = await database.Message.findAll({ 
                attributes: ['id', 'content', 'createdAt'],
                where: { conversation_id: id },
                raw: true
            });
            
            let allMessages = [];

            messages.forEach(message => {
                let messageData = {};
                const messageDate = dates.formatToDMY(message.createdAt.toISOString().split('T')[0]);
                const time = message.createdAt.toISOString().split('T')[1];
                const messageTime = (time.split(':')[0] - 3)+ ":" + time.split(':')[1];

                messageData.id = message.id;
                messageData.content = message.content;
                messageData.messageDate = messageDate;
                messageData.messageTime = messageTime; 
                
                allMessages.push(messageData);
            });


            const responseData = {
                conversation_id: conversation.id,
                conversation_name: conversation.name,
                category_name: conversation.Category.name,
                messages: allMessages
            }

            return res.status(200).send(responseData);
        } catch (error) {
            return res.status(500).send({ message: error.message })
        }
    }

    static async verifyCategory(req, res) {
        try {
            const data = req.body;

            return res.status(200).send(service.verifyCategory(data.content));
        } catch (error) {
            console.log(error);
            return res.status(500).send({ message: error.message })
        }
    }
    

}

module.exports = ConversationController;