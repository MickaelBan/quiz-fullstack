<template>
  <div v-if="!editMode">
    <div v-for="(question, index) in questionsList" v-bind:key="question.id">
      <div class="QuestionDislayAdmin">
        <div class="title">
          <h1>Question {{ index + 1 }}</h1>
        </div>
        <QuestionDisplay :question=question :adminMode=true />
        <div class="button" id="edit">
          <input type="submit" value="Edit question" v-on:click="editQuestion(question)">
        </div>
        <div class="button" id="delete">
          <input type="submit" value="Remove question" v-on:click="deleteQuestion(question)">
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <EditQuestionDisplay :question="selectedQuestion" @cancel="back" />
  </div>





</template>

<style>
.QuestionDislayAdmin {
  width: 100%;
  margin: 100px 0px;
}
</style>


<script>
import AdminStorageService from '../services/AdminStorageService';
import QuizApiService from '../services/QuizApiService';
import QuestionDisplay from './QuestionDisplay.vue';
import EditQuestionDisplay from './EditQuestionDisplay.vue';

export default {
  components: { QuestionDisplay, EditQuestionDisplay },
  data() {
    var questionsList = []
    var sizeQuestionsList = 0
    var selectedQuestion = {}
    var editMode = false
    return { questionsList, sizeQuestionsList, editMode, selectedQuestion }
  },
  async created() {
    var reponce = await QuizApiService.getQuizInfo()
    this.sizeQuestionsList = reponce.data.size
    this.questionsList = await this.setQuestionsList()
    console.log(this.questionsList)
    console.log("created display question")
  },
  methods: {
    async deleteQuestion(question) {
      let token = AdminStorageService.getToken();
      if (token !== undefined) {
        console.log("remove")
        await QuizApiService.delQuestion(token, question.id);
        this.$router.go();
      }
    },
    async setQuestionsList() {
      var list = []
      for (var i = 1; i <= this.sizeQuestionsList; i++) {
        var question = await QuizApiService.getQuestionByPosition(i)
        list.push(question.data)
      }
      return list
    },
    editQuestion(question) {
      this.editMode = true
      this.selectedQuestion = question
    },
    back() {
      this.editMode = false
    }

  }
}
</script>