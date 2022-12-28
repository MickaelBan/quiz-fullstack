<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }}</h1>
    <body>
        <QuestionDisplay :question="currentQuestion" @click-on-answer="answerClickedHandler" />
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
            id: null,
            title: "",
            text: "",
            image: "",
            position: null,
            possibleAnswers: []
        };
        let currentQuestionPosition = 0;
        let totalNumberOfQuestion = 0;
        return {
            currentQuestion,currentQuestionPosition,totalNumberOfQuestion
        };
    },    
    async created() {
        this.currentQuestionPosition  = 1 ;
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
        async answerClickedHandler(indexQuestion){
            answer = this.currentQuestion.possibleAnswers[indexQuestion]
        },
        async endQuiz(){}
    }

}
</script>