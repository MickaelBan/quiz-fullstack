
<template>
  <body>    
    <div class="component1">
      <h1>New quiz</h1>
    </div>

    <div class="component1">
      <h3>Choose your name</h3>
    </div>

    <div class="component">
      <label for="pName">Player Name</label>
      <input type="text" id="pName" name="playerName" placeholder="Your name..">
      <input type="submit" value="Submit">
    </div>

  </body>
</template>

<style>
.component1{
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

.component{
  border-radius: 5px;
  background-color: #f2f2f2;
  color : black;
  padding: 20px;
}
</style>


<script>

</script>
