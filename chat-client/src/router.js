import { createRouter, createWebHashHistory } from "vue-router";
import HomeComponent from "@/pages/Home.vue";
import LoginComponent from "@/pages/Login.vue";


const routes = [{
    path: "/", component: HomeComponent, name: "home"
}, {
    path: "/login", component: LoginComponent, name: "login"
}];


const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
});


export default router;
