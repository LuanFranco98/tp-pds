import Vue from 'vue'

import PostbyCategory from './PostbyCategory.vue'

Vue.config.productionTip = false

import axios from 'axios'
Vue.prototype.$http = axios
Vue.prototype.$api_url = process.env.VUE_APP_API_HOST

new Vue({
  render: h => h(PostbyCategory),
}).$mount('#app')
