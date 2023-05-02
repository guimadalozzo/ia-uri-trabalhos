const express = require('express');
const app = express();
const nunjucks = require('nunjucks');
const bodyParser = require('body-parser');
const axios = require('axios');

var port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log('listen on port: ' + port);
});

let env = nunjucks.configure('views', {
    autoescape: true,
    express: app
});

app.set('engine', env);

require('useful-nunjucks-filters')(env);

app.use(bodyParser.json());       // to support JSON-encoded bodies

app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
    extended: true
}));

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index.html');
});

app.get('/getInfo', async(req, res) => {
    console.log("Backend node");

    await axios.get('http://localhost:5000/getWords')
    .then((response) => {
        console.log(response.data);
        const obj = {
            "status": 200,
            "text": response.data
        }
        res.send(obj)
    })
    .catch((error) => {
        console.error(error);

        const obj = {
            "status": 500,
            "error": error
        }

        res.send(obj)
    });


});