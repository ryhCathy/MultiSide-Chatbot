<script>
export default {
  name: "list_com",
  computed: {
    sessions() {
      return this.$store.state.sessions
    },
    current_session(){
      return this.$store.state.current_session
    }
  },
  mounted() {
    this.$socket.onFriendOnline((result) => {
      // console.log(result);
      let user = result.user;
      // this.$chat.addSession(user);
      this.$store.commit('ADD_SESSION', user)
    })
    
    this.$socket.onFriendOffline((result) => {
      // console.log(result);
      let user = result.user;
      this.$store.commit('DELETE_SESSION', user)
    })
  },
  methods: {
    onSelectSession(session) {
      this.$store.commit("SET_CURRENT_SESSION", session);
    }
  }
};
</script>

<template>
  <div class="list">
    <ul>
      <li 
        v-for="session in sessions" 
        @click="onSelectSession(session)" 
        :class="{'active': (current_session && session.user.sid == current_session.user.sid)}"
        :key="session.user.sid"
      >
        <img class="avatar" width="30" height="30" :alt="session.user.username"
          :src="$socket.server_host + session.user.avatar">
        <el-badge :value="session.unread" class="item" :hidden="session.unread == 0">
          <p class="name">{{ session.user.username }}({{ session.user.ip }})</p>
        </el-badge>
      </li>
    </ul>
  </div>
</template>

<style scoped lang="less">
.list {
  li {
    padding: 12px 15px;
    border-bottom: solid 1px #ddd;
    cursor: pointer;
    transition: background-color 0.1s;

    &:hover {
      background-color: rgba(255, 255, 255, 0.03);
    }

    &.active {
      background-color: rgba(255, 255, 255, 0.1);
    }

    .unread-count {
      padding: 2px 5px;
    }
  }

  .avatar,
  .name {
    vertical-align: middle;
  }

  .avatar {
    border-radius: 2px;
  }

  .name {
    display: inline-block;
    margin: 0 0 0 15px;
  }
}
</style>
