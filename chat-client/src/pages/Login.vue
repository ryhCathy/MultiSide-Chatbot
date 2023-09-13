<template>
    <div class="login-container">
      <el-form ref="form" :model="form" class="login-main">
        <h1 class="h1_stylish" >Hello Chatbot</h1>
        <el-form-item>
          <el-input v-model="form.username" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item style="text-align: right">
          <el-button type="primary" @click="onSubmit">Login</el-button>
        </el-form-item>
      </el-form>
    </div>
  </template>
  
  <script>
  import {ElMessage} from "element-plus";
  export default {
    name: "LoginComponent",
    data() {
      return {
        form: {
          username: ""
        }
      };
    },
    mounted() {
  
      },
    methods: {
        onSubmit() {
            if(!this.form.username){
                ElMessage.error("Please enter your username");
                   return;
            } // now send by socket request instead of socket
            // check if 
            // send the event of "login": emit
            if(!this.$socket.connected){
                this.$socket.connect();
            }
            // this.$socket.emit("login", {"username": this.form.username}, (result) => {
            //   console.log(result);
            // });
            this.$socket.emitLogin(this.form.username, (result) => {
              console.log(result);
              if(result['code'] == 200){
                    //console.log("get")
                    //const user = result['data']; // in pycharm backend: the data returned is just the username
                    //console.log(user['username'])
                    const data = result['data'];
                    const user = data['user'];
                    const online_users = data['online_users'];
                    this.$store.commit("SET_SESSIONS", online_users); // should be in " "
                    this.$store.commit("SET_USER", user);
                    this.$router.push({'name': "home"}); // direct to "home"
                } else {
                    console.log("error")
                    console.log(result['message'])
                    ElMessage.error(result['message']);
                }
            });
        }
    }
  };
  </script>
  
  <style scoped>
  html,
  body {
    height: 100%;
  }
  .login-container {
    width: 100vw;
    height: 100vh;
    background-image: url("../assets/login_bg1.jpeg");
    background-size: cover;
    background-color: rgba(0, 0, 0, 0.7); /* Set background color with opacity */
    overflow: hidden;
  }
  
  .login-container .login-main {
    border-radius: 5px;
    background-clip: padding-box;
    margin: 280px auto;
    width: 350px;
    padding: 35px 35px 15px;
    background: #F3B0C3; 
    background: rgba(243, 176, 195, 0); /* Set fully transparent background color */
    /* border: 1px solid #D4F0F0; */
    /* -webkit-box-shadow: 0 0 25px #FFCCB6; */
    /* box-shadow: 0 0 25px #F3B0C3; */
  }

  .h1_stylish {
    text-align: center;
    font-family: 'Brush Script MT', cursive;
    font-size: 60px;
    color: #EE9C6C;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  }

  </style>
  








<!-- <template>
    <div>
        <h1>Login</h1>
    </div>
</template>  

<script>
export default {
    name: "LoginComponent"
}
</script>

<style lang="">

</style> -->

