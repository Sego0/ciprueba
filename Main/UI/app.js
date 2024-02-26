const routes=[
    {path:'/employee',component:employee},
    {path:'/device',component:device},
    {path:'/employeedevice',component:employeedevice},
]

const router=new VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})

const app = Vue.createApp({})
app.use(router)
app.mount('#app')