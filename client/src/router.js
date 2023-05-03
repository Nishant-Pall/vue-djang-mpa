import Vue from "vue";
import VueRouter from "vue-router";
import AnagramGame from "./apps/AnagramGame.vue";
import MathGame from "./apps/MathGame.vue";

Vue.use(VueRouter);
const routes = [
	{
		path: "/anagram-game",
		component: AnagramGame,
	},
	{
		path: "/math-game",
		component: MathGame,
	},
];

const router = new VueRouter({
	mode: "history",
	routes: routes,
});

export default router;
