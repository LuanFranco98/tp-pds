import Vue from 'vue'

import LoginUsuario from './LoginUsuario.vue'

Vue.config.productionTip = false

import axios from 'axios'
Vue.prototype.$http = axios
Vue.prototype.$api_url = process.env.VUE_APP_API_HOST

new Vue({
  render: h => h(LoginUsuario),
}).$mount('#app')
