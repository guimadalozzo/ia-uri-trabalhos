const { Router } = require('express');
const AuthenticationController = require('../controllers/AuthenticationController');
const UserController = require('../controllers/UserController');

const router = Router();

router.get('/authentication', AuthenticationController.welcome);

router.post('/authenticate', AuthenticationController.authenticate);

router.post('/users', UserController.create);

module.exports = router;