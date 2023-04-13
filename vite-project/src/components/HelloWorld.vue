<script>

import { darkTheme } from "naive-ui";

export default {
  name: "HelloWorld",
  data() {
    return {
      setting: {
        'ws_uri': 'ws://localhost:8765'
      },
      cmd: '0000000000',
      showModal: false,
      showRecord: false,
      clear_loading: false,
      send_loading: false,
      open_loading: false,
      close_loading: false,
      socket: null,
      log: [],
      theme: null,
      activeDarkTheme: true
    }
  },
  methods: {
    handleClearBtn: function() {
      this.clear_loading = true 
      setTimeout(() => {
        this.cmd='0000000000'; 
        this.clear_loading=false;
      }, 100)
    },
    handleSendBtn: async function () {
      if (this.socket == null) {
        alert("端口未打开")
      }
      else {
        this.send_loading = true
        setTimeout(() => {
          this.log.push('> ' + this.cmd)
          this.socket.send(this.cmd);
          this.send_loading=false;
        }, 400)
      }
    },
    watchSocket: function () {
      var socket = new WebSocket(this.setting.ws_uri);
      socket.onopen = (e) => {
        socket.send('Kevin')
        // this.log = 'Open Socket' + '\n'
      }
      socket.onmessage = (e) => {
        console.log('SOCKET OPEN FAIL:' + e.data)
        this.log.push('< ' + e.data)
      }
      socket.onerror = (e) => {
        console.log(e)
        this.log.push(e)
      }
      return socket
    },
    openSocket: function () {
      this.open_loading = true
      setTimeout(() => {
        this.socket = this.watchSocket()
        this.open_loading = false
      }, 500);
    },
    closeSocket: function () {
      this.close_loading = true
      setTimeout(() => {
        this.socket = null
        this.close_loading = false
      }, 500);
    }
  },
  setup() {
    return {
      darkTheme
    }
  }
}

</script>

<template>
  <!-- 隐藏面板 -->
  <!-- 设置面板 -->
  <n-modal v-model:show="showModal">
    <n-card
      style="width: 600px"
      title="设置"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
    >
      <template #header-extra>
        <div style="cursor: pointer;">Opps</div>
      </template>
        <!-- ws地址 -->
        <n-h4>地址</n-h4>
        <n-auto-complete
          v-model:value="setting['ws_uri']"
          placeholder="wsi"
          :render-label="renderLabel"
        />

    </n-card>
  </n-modal>
  <!-- Log面板 -->
  <n-modal v-model:show="showRecord">
    <n-card
      style="width: 600px"
      title="记录"
      :bordered="false"
      size="huge"
      role="dialog"
      aria-modal="true"
    >
      <template #header-extra>
        <div style="cursor: pointer;">Opps</div>
      </template>
      <n-card title="Log">
        <div v-for="item in log" >
          {{ item }}
        </div>
      </n-card>
    </n-card>
  </n-modal>

  <n-space>
    <h3 @click="() => {showModal=true}" style="cursor: pointer;">设置</h3>
    <h3 @click="() => {showRecord=true}" style="cursor: pointer;">记录</h3>
    <h3 @click="() => {showPlus=true}" style="cursor: pointer;">...</h3>
  </n-space>



  <h1>{{ cmd }}</h1>
  <n-space vertical>
    <n-grid x-gap="100" :cols="5" id="rotate-options">
      <n-gi>
        <n-h3>A</n-h3>
        <n-space vertical>
          <n-button @click="() => {cmd = '01' + cmd.substring(2,10);}">正转</n-button>
          <n-button @click="() => {cmd = '00' + cmd.substring(2,10);}">静止</n-button>
          <n-button @click="() => {cmd = '10' + cmd.substring(2,10);}">反转</n-button>
        </n-space>
      </n-gi>
      <n-gi>
        <n-h3>B</n-h3>
        <n-space vertical>
          <n-button @click="() => {cmd = cmd.substring(0, 2) + '01' + cmd.substring(4,10);}">正转</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 2) + '00' + cmd.substring(4,10);}">静止</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 2) + '10' + cmd.substring(4,10);}">反转</n-button>
        </n-space>
      </n-gi>
      <n-gi>
        <n-h3>C</n-h3>
        <n-space vertical>
          <n-button @click="() => {cmd = cmd.substring(0, 4) + '01' + cmd.substring(6,10);}">正转</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 4) + '00' + cmd.substring(6,10);}">静止</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 4) + '10' + cmd.substring(6,10);}">反转</n-button>
        </n-space>
      </n-gi>
      <n-gi>
        <n-h3>D</n-h3>
        <n-space vertical>
          <n-button @click="() => {cmd = cmd.substring(0, 6) + '01' + cmd.substring(8,10);}">正转</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 6) + '00' + cmd.substring(8,10);}">静止</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 6) + '10' + cmd.substring(8,10);}">反转</n-button>
        </n-space>
      </n-gi>
      <n-gi>
        <n-h3>E</n-h3>
        <n-space vertical>
          <n-button @click="() => {cmd = cmd.substring(0, 8) + '01';}">正转</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 8) + '00';}">静止</n-button>
          <n-button @click="() => {cmd = cmd.substring(0, 8) + '10';}">反转</n-button>
        </n-space>
      </n-gi>
    </n-grid>
    <n-grid x-gap="10" :cols="4" style="margin-top: 50px;">
      <n-gi>
        <n-button size="large" color="#3b8361" :loading="open_loading" @click="openSocket">打开</n-button>
      </n-gi>
      <n-gi>
        <n-button size="large" color="#387f60" :loading="close_loading" @click="closeSocket">关闭</n-button>
      </n-gi>
      <n-gi>
        <n-button size="large" color="#2c745c" :loading="clear_loading" @click="handleClearBtn">清零</n-button>
      </n-gi>
      <n-gi>
        <n-button size="large" color="#1e6858" :loading="send_loading" @click="handleSendBtn">发送</n-button>
      </n-gi>
    </n-grid>
  </n-space>



  <n-h4 class="copyright" style="position: absolute; bottom: 5px; left: 50%; transform: translate(-50%, 0);">@sitdownkevin</n-h4>

</template>

<style scoped>

</style>
