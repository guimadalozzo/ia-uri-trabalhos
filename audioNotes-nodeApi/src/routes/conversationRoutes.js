const { Router } = require('express');
const ConversationController = require('../controllers/ConversationController');

const router = Router();

router.post('/messages', ConversationController.storageMessage);

router.post('/verifyCategory', ConversationController.verifyCategory);

router.get('/conversations', ConversationController.readAll);

router.get('/conversations/:id', ConversationController.readConversation);

module.exports = router;