const trainingData = require('../../trainingData.json');

const natural = require("natural"); 
class ConversationService {
    
    static verifyCategory(data) {
        // Defining the categories
        const categories = new natural.BayesClassifier();

        // Adding the categories
        categories.addDocument("ideia", ["ideias", "pensamento", "profissão"]);
        categories.addDocument("estudo", ["estudar", "escola", "faculdade"]);
        categories.addDocument("casa", ["morar", "residência", "lar", "casa"]);
        categories.addDocument("trabalho", ["emprego", "empresa", "profissão"]);

        // Defining the classifier based on categories
        const classifier = new natural.BayesClassifier();

        // Training the classifier with examples from each "category"
        trainingData.forEach((example) => classifier.addDocument(example.text, example.category));
        classifier.train();

       // Sorting a text
        const category = classifier.classify(data);
        
        return category;
    }

    static createConversationForm(name, categoryAlias, userId) {
        let categoryId;
        
        switch (categoryAlias) {
            case 'estudo':
                categoryId = 2;
                break;
            case 'casa':
                categoryId = 3;
                break;
            case 'trabalho':
                categoryId = 4;
                break;
            default:
                categoryId = 1;
                break;
        }

       return {
            name: name,
            category_id: categoryId,
            user_id: userId
        };
    }

    static createMessageForm(content, conversation_id) {
        return {
            content: content,
            conversation_id: conversation_id
        }
    }

    static createNameByText(content, maxLength = 3) {
        const contentArray = content.split(' ')
        let name = "";
        let i = 0; 
        contentArray.forEach(content => {
            if (i == maxLength) return false;
            name += content + " ";
            i++;
        })
        return name.trimEnd();
    }

}

module.exports = ConversationService;