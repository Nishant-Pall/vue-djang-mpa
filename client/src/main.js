import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { axios } from "vue/types/umd";
import VueAxios from "vue-axios";

Vue.config.productionTip = false;

new Vue({
	render: (h) => h(App),
	router,
	axios,
	VueAxios,
}).$mount("#app");
