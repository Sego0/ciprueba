const employee={templates:'<h1>hola</h1>',

data(){
    return{
        employee:[]
    }
},
methods:{
    refreshData(){
        axios.get(variables.API_URL+'employee')
        .then((response)=>{
            this.employee=response.data;
        });
    }
},
mounted:function(){
    this.refreshData();
}


}
