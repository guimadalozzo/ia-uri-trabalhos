const cors = require('cors');
const publicRoutes = require('./publicRoutes');
const userRoutes = require('./userRoutes');
const conversationRoutes = require('./conversationRoutes');
const jwt = require('jsonwebtoken');

module.exports = (app, express) => {
    app.use(cors());
    app.use(express.json())
    app.use(express.urlencoded({ extended: true}))

    app.get('/', (req, res) => res.send('Welcome to API-AudioNotes'));
    
    app.use(publicRoutes);

    // ONLY AUTHENTICATE ACCESS
    app.use((req, res, next) => {
        let token = req.headers.authorization;
        if (!token) return res.sendStatus(401);
        token = token.replace('Bearer ', '');
    
        jwt.verify(token, process.env.JWT_SECRET, (err, payload) => {
            if(err) return res.sendStatus(401);
            req.userId = payload.userId;
            next();
        })
    })

    app.use(userRoutes);
    app.use(conversationRoutes);
}