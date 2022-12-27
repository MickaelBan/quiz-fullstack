
<template>
  <body>    
    <div class="cpnt1">
      <h1>New quiz</h1>
    </div>

    <div class="cpnt1">
      <h3>Choose your name</h3>
    </div>

    <div class="cpnt">
      <label for="pName">Player Name</label>
      <input type="text" v-model="username" id="pName" name="playerName" placeholder="Your name..">
      <input type="submit" value="launch quiz" v-on:click="launchNewQuiz">
    </div>

  </body>
</template>


<script>
import participationStorageService from "../services/ParticipationStorageService";

export default {
  data(){
    let username = ''
    return {
      username
    }
  },
  methods:{
    launchNewQuiz(){
      participationStorageService.savePlayerName(this.username)
      console.log("save name")
      console.log("launch new quiz")
      this.$router.push('/questions');
    }
  }

}
</script>



<style>
.cpnt1{
  padding: 20px;
  text-align: center
}

input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.cpnt{
  border-radius: 5px;
  background-color: #f2f2f2;
  color : black;
  padding: 20px;
}
</style>
