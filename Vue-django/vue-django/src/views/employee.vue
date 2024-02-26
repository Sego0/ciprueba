<template>
<br>
<div class="container">
  <div class="input-group">
    <button type="button" class="btn btn-success btn-md" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Agregar +</button>
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">Nuevo Empleado:</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="input-group mb-3">
                <div class="mb-3">
                  <label for="Id_rut" class="col-form-label">Rut:</label>
                  <input type="number" class="form-control" id="Id_rut" v-model="Id_rut">
                </div>
                <div class="mb-3">
                  <label for="Name" class="col-form-label">Nombre:</label>
                  <input type="text" class="form-control" id="Name" v-model="Name">
                </div>
                <div class="mb-3">
                  <label for="Area" class="col-form-label">Area:</label>
                  <input type="text" class="form-control" id="Area" v-model="Area">
                </div>
                <div class="mb-3">
                  <label for="Mail" class="col-form-label">Mail:</label>
                  <input type="text" class="form-control" id="Mail" v-model="Mail">
                </div>
                <div class="mb-3">
                  <label for="status" class="col-form-label">Estatus:</label>
                  <select class="form-select" id="status" v-model="status">
                    <option value="Activo">Activo</option>
                    <option value="Inactivo">Inactivo</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="last_change" class="col-form-label">Creado por:</label>
                  <select class="form-select" id="last_change" v-model="last_change">
                    <option value="1">Admin</option>
                  </select>
                </div>
              </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                  <button type="button" class="btn btn-success"  @click="sendData">Agregar</button>
                </div>
              </form>
            </div>
          </div>
        </div>  
      </div>
      <input type="text" class="form-control" id="nombre" aria-label="Text input with segmented dropdown button" placeholder="Ingrese el nombre . . . " v-model="nombre">
      <button type="button" class="btn btn-outline-secondary btn-lg" id="nombre" @click="namefilter(nombre)">Buscar</button>
      <input type="text" class="form-control" id="rut" aria-label="Text input with segmented dropdown button" placeholder="Ingrese el rut . . . " v-model="rut">
      <button type="button" class="btn btn-outline-secondary btn-lg" id="nombre" @click="rutfilter(rut)">Buscar</button>
      <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
        <span class="visually-hidden">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu dropdown-menu-end">
        <li><a class="dropdown-item" @click="statusfilter('Activo')">Todos los activos</a></li>
        <li><a class="dropdown-item" @click="statusfilter('Inactivo')">Todos los inactivos</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" @click="refreshData()" >Todos los Empleados</a></li>
      </ul>
    </div>
    <br>

  </div>
  <div class="container" style="text-align:center;"> 
  <table class="table table_hover" border="0" style="margin: 0 auto;">  
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Nombre</th>
      <th scope="col">Area</th>
      <th scope="col">Mail</th>
      <th scope="col">Estatus</th>
      <th scope="col">Opciones</th>
    </tr>
  </thead>
  <tbody v-for="employe in employees.results" :key="employe.id">
    <tr>
      <th scope="row">{{ employe.Id_rut }}</th>
      <td>{{ employe.Name }}</td>
      <td>{{ employe.Area }}</td>
      <td>{{ employe.Mail }}</td>
      <td>{{ employe.status }}</td>
      <td>
        <div class="btn-group" role="group" aria-label="Basic example">

          <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleMod" data-bs-whatever="@getbootstrap" @click="getData(employe.Id_rut)">Editar</button>
          
          <div class="modal fade" id="exampleMod" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Modificar informacion:</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
            <div class="modal-body">
              <form>
                <div class="input-group mb-3">
                <div class="mb-3">
                  <label for="Id_rut" class="col-form-label">Rut:</label>
                  <input type="number" class="form-control" id="Id_rut" v-model="emple.Id_rut">
                </div>
                <div class="mb-3">
                  <label for="Name" class="col-form-label">Nombre:</label>
                  <input type="text" class="form-control" id="Name" v-model="emple.Name">
                </div>
                <div class="mb-3">
                  <label for="Area" class="col-form-label">Area:</label>
                  <input type="text" class="form-control" id="Area" v-model="emple.Area">
                </div>
                <div class="mb-3">
                  <label for="Mail" class="col-form-label">Mail:</label>
                  <input type="text" class="form-control" id="Mail" v-model="emple.Mail">
                </div>
                <div class="mb-3">
                  <label for="status" class="col-form-label">Estatus:</label>
                  <select class="form-select" id="status" v-model="emple.status">
                    <option value="Activo">Activo</option>
                    <option value="Inactivo">Inactivo</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="last_change" class="col-form-label">Creado por:</label>
                  <select class="form-select" id="last_change" v-model="emple.last_change">
                    <option value="1">Admin</option>
                  </select>
                </div>
              </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                  <button type="button" class="btn btn-success" @click="modifiedData" >Modificar</button>
                </div>
              </form>
            </div>
          </div>
        </div>  
      </div>
        </div>
      </td>
    </tr>
  </tbody>
</table>
<br>
<div>
<nav aria-label="Page navigation example">
  <ul class="pagination justify-content-center">
    <li  v-if="employees.count" scope="row" class="page-item" v-for="page in Math.ceil(employees.count/50)">
      <a type="button" class="page-link" @click="getPage(page)">{{ page }}</a></li>
  </ul>
</nav>
</div>
  <br>
  </div>

</template>

<script>
    import axios from 'axios'


    export default{
      name: 'NavigationComponent',

      data(){
        return {
            Id_rut:0,
            Name:'',
            Area:'',
            Mail:'',
            status:'',
            last_change:1,
            employees: [],
            emple:[],
            nombre:'',
        };
      },
      methods:{
        refreshData(){
          axios.get('http://127.0.0.1:8000/api/api/employee/')
          .then((response) => {
            this.employees = response.data;});
        },

        async namefilter(name){
          await axios.get('http://127.0.0.1:8000/api/api/employee/?Name='+name)
          .then((response) => {
            this.employees = response.data;});  
        },

        async rutfilter(rut){
          await axios.get('http://127.0.0.1:8000/api/api/employee/?Id_rut='+rut)
          .then((response) => {
            this.employees = response.data;});  
        },

        async statusfilter(status){
          await axios.get('http://127.0.0.1:8000/api/api/employee/?status='+status)
          .then((response) => {
            this.employees = response.data;});
        },
        async getData(id){
          await axios.get('http://127.0.0.1:8000/api/api/employee/'+id)
          .then(response => {
            this.emple = response.data;});
        },
        async getPage (page){
          await axios.get('http://127.0.0.1:8000/api/api/employee/?page='+page)
          .then(response => {
            this.employees = response.data;
            window.scrollTo({top:0,behavior:'smooth'});
          });

        },
        async sendData(){
          const datatosend ={
            Id_rut:this.Id_rut,
            Name:this.Name,
            Area:this.Area,
            Mail:this.Mail,
            status:this.status,
            last_change:this.last_change
          };
          await axios.post('http://127.0.0.1:8000/api/api/employee/',datatosend)
          .then(response => {console.log(response.data);window.location.reload()
          }).catch(error => {console.error('Error en el envio', error);
          alert("Error en el envio ") ;
        });
        },
        async deleteData(id){
          await axios.delete('http://127.0.0.1:8000/api/api/employee/'+id)
          .then(response => {
            console.log(response.data);
            this.refreshData();
            window.location.reload()})
            .catch(error => {
              console.error('Error al eliminar',error);
            alert("Error en el borrado ") ;
            });
        },
        async modifiedData(){
          const modData ={
            Id_rut:this.emple.Id_rut,
            Name:this.emple.Name,
            Area:this.emple.Area,
            Mail:this.emple.Mail,
            status:this.emple.status,
            last_change:this.emple.last_change
          };
          await axios.put('http://127.0.0.1:8000/api/api/employee/'+this.emple.Id_rut+'/',modData) 
          .then(response => {console.log(response.data);window.location.reload()
          }).catch(error => {console.error('Error en el envio', error);
            alert("Error en la modificacion ") ; 
        });
        },


      },
      mounted(){
          this.refreshData();
      }

    }
</script>

<style>

</style>
