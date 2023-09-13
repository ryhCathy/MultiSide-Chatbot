<template>
  <div class="home-container">
    <!-- <template v-if="$chat.user">  -->
    <template v-if="$store.state.user">
      <div class="sidebar">
            <card_com></card_com>
            <list_com></list_com>
        </div>
        <div class="main">
            <message_com></message_com>
            <chat_com></chat_com>
        </div>
    </template>
  </div>
</template>

<script>
import card_com from '@/components/card';
import list_com from '@/components/list';
import chat_com from '@/components/text';
import message_com from '@/components/message';

export default {
  name: "HomeComponent",
  created() {},
  mounted(){
    if(!this.$store.getters.logined) {
      this.$router.push({name: "login"}); // direct to login page
      return;
    }

  },
  components: {
    card_com, list_com, chat_com, message_com
  }
};
</script>

<style>
body, html{
  height: 100%;
    overflow: hidden;
}
body{
  font: 14px/1.4em 'Helvetica Neue', Helvetica, 'Microsoft Yahei', Arial, sans-serif;
  background: #f5f5f5 url("../assets/chat_bg1.jpeg") no-repeat center;
  background-color: rgba(245, 245, 245, 0.3); 
  background-size: cover;
}
ul{
  list-style: none;
}
</style>

<style scoped lang="less">
.home-container {
    // margin-left: 20px; 
    margin-left: 30px; 
    margin-top: 30px; 
    width: 800px;
    height: 600px;

    overflow: hidden;
    border-radius: 20px;

    .sidebar, .main {
        height: 100%;
    }
    .sidebar {
        float: left;
        width: 200px;
        color: #56351E;
        background-color: rgba(231, 151, 150, 0.8);
    }
    .main {
        position: relative;
        overflow: hidden;
        background-color: rgba(245, 206, 199, 0.6);
        box-shadow: 0 0 10px rgba(204, 171, 219, 0.9);
    }
    .text {
        position: absolute;
        width: 100%;
        bottom: 0;
        left: 0;
    }
    .message {
        height: ~'calc(100% - 160px)';
    }
}
</style>
