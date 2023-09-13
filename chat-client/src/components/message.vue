<script>
export default {
  name: "message_com",
  computed: {
    current_session(){
      return this.$store.state.current_session
    },
    user(){
      return this.$store.state.user
    }
  },
  methods: {
    timeFormat(date) {
			if (typeof date === "string") {
				date = new Date(date);
			}
			return date.getHours() + ":" + date.getMinutes();
		}
  },
	updated(){
    this.$nextTick(() => {
      var container = this.$refs.el;
      container.scrollTop = container.scrollHeight;
    });
	},
  mounted() {
    this.$socket.onReceiveMessage( (result) => { // get from the backgound
      //console.log(result) //  {message, from}
      const sid = result['from'];
      const message = result['message'];
      //console.log(sid, message) 
      this.$store.commit("RECEIVE_MESSAGE", {"sid": sid, "content": message})
    });
  }
};
</script>

<template>
  <div class="message" ref="el">
    <ul v-if="current_session">
      <li v-for="(message, index) in current_session.messages" :key="index">
        <p class="time">
          <span>{{ timeFormat(message.date) }}</span>
        </p>
        <div :class="{'main': true, 'self': message.self}">
          <!-- <p>{{ message.self }}</p> -->
          <img
            class="avatar"
            width="30"
            height="30"
            :src="$socket.server_host+user.avatar" 
          />
          <div class="text">{{message.content}}</div>
        </div>
      </li>

    </ul>
  </div>
</template>

<style lang="less" scoped>
.message {
  padding: 10px 15px;
  overflow-y: scroll;

  li {
    margin-bottom: 15px;
  }
  .time {
    margin: 7px 0;
    text-align: center;

    > span {
      display: inline-block;
      padding: 0 18px;
      font-size: 12px;
      color: rgba(174, 127, 108, 0.5);
      border-radius: 2px;
      background-color: rgba(220, 220, 220, 0.5);
    }
  }
  .avatar {
    float: left;
    margin: 0 10px 0 0;
    border-radius: 3px;
  }
  .text {
    display: inline-block;
    position: relative;
    padding: 0 10px;
    max-width: ~"calc(100% - 40px)";
    min-height: 30px;
    line-height: 2.5;
    font-size: 15px;
    text-align: left;
    word-break: break-all;
    background-color: rgba(174, 127, 108, 0.5);
    border-radius: 4px;

    &:before {
      content: " ";
      position: absolute;
      top: 9px;
      right: 100%;
      border: 6px solid transparent;
      border-right-color: rgba(174, 127, 108, 0.5);
    }
  }

  .self {
    text-align: right;

    .avatar {
      float: right;
      margin: 0 0 0 10px;
    }
    .text {
      background-color: rgba(172, 224, 221, 0.5);

      &:before {
        right: inherit;
        left: 100%;
        border-right-color: transparent;
        border-left-color:  #F5CEC7;
      }
    }
  }
}
</style>
