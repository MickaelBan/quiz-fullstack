<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <body>
        <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
    </body>
</template>

<script>
import QuestionDisplay from '../views/QuestionDisplay.vue';
import QuizApiService from '../services/QuizApiService'
export default { 
    components: {
        QuestionDisplay
    },
    data() {
        let currentQuestion = {
            id: 0,
            title: "",
            text: "",
            image: "",
            position: 0,
            possibleAnswers: []
        };
        let currentQuestionPosition = 0;
        let totalNumberOfQuestion = 0;
        let listAnswers = [];
        return {
            currentQuestion,currentQuestionPosition,totalNumberOfQuestion,listAnswers
        };
    },    
    async created() {
        this.currentQuestionPosition  = 5 ;
        this.currentQuestion = await this.loadQuestionByPosition(this.currentQuestionPosition)
        let reponce = await QuizApiService.getQuizInfo()
        this.totalNumberOfQuestion = reponce.data.size
        console.log("question manager created")
    },
    methods:{
        async loadQuestionByPosition(position){
            let reponse = await QuizApiService.getQuestionByPosition(position)
            return reponse.data
        },
        async answerClickedHandler(answer){
            this.listAnswers.push(answer)
            if (this.currentQuestion == this.totalNumberOfQuestion){
                this.endQuiz()
                console.log("end")
            }
            else {
                this.currentQuestionPosition += 1;
                console.log(this.currentQuestionPosition)
                let nextQuestion = await this.loadQuestionByPosition(this.currentQuestionPosition);
                this.currentQuestion = nextQuestion;
                
            }

        },
        async endQuiz(){}
    }

}
</script>