<template>
<br>
<div class="container">
  <div class="input-group">
  <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Agregar +</button>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">Nuevo dispositivo:</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="input-group mb-3">
                <div class="mb-3">
                  <label for="id_device" class="col-form-label">Numero de serie:</label>
                  <input type="text" class="form-control" id="id_device" v-model="id_device">
                </div>
                <div  class="mb-3">
                  <label for="id_type" class="col-form-label">Tipo:</label>
                  <select class="form-select" id="id_type" v-model="id_type">
                    <option value="1">Notebook</option>
                    <option value="2">Telefono</option>
                    <option value="3">Monitor</option>
                  </select>
                  </div>
                <div class="mb-3">
                  <label for="Modelo" class="col-form-label">Modelo:</label>
                  <input type="text" class="form-control" id="Modelo" v-model="Model">
                </div>
                <div class="mb-3">
                  <label for="Waranty" class="col-form-label">Garantia:</label>
                  <input type="date" class="form-control" id="Waranty" v-model="Waranty">
                </div>
                <div class="mb-3">
                  <label for="Number" class="col-form-label">Numero:</label>
                  <input type="number" class="form-control" id="Number" v-model="Number">
                </div>
                <div class="mb-3">
                  <label for="Status" class="col-form-label">Estatus:</label>
                  <select class="form-select" id="Status" v-model="Status">
                    <option value="Normal">Normal</option>
                    <option value="Danado">Dañado</option>
                    <option value="Alto">Alto uso</option>
                    <option value="Operativo">No operativo</option>
                    <option value="No">No especifica</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="Asigned" class="col-form-label">Asignado?:</label>
                  <select class="form-select" id="Asigned" v-model="Assigned">
                    <option value="true">Si</option>
                    <option value="false">No</option>
                  </select>
                </div>
              </div>
              <div class="mb-3">
                  <label for="last_change" class="col-form-label">Last_change:</label>
                  <select class="form-select" id="last_change" v-model="last_change">
                    <option value="1">Admin</option>
                  </select>
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

      <input type="text" class="form-control" aria-label="Text input with segmented dropdown button" placeholder="Ingrese el numero de serie . . . " v-model="serialnumber">
      <button type="button" class="btn btn-outline-secondary btn-lg" @click="filterSn(serialnumber)">Buscar</button>
      <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
        <span class="visually-hidden">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu dropdown-menu-end">
        <li><a class="dropdown-item" @click="filterAssigned('True')">Asignados</a></li>
        <li><a class="dropdown-item" @click="filterTypeAssigned('True','1')">Computadores asignados</a></li>
        <li><a class="dropdown-item" @click="filterTypeAssigned('True','2')">Telefonos asignados</a></li>
        <li><a class="dropdown-item" @click="filterTypeAssigned('True','3')">Monitores asignados</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item"  @click="filterAssigned('False')">No asignados</a></li>
        <li><a class="dropdown-item" @click="filterTypeAssigned('False','1')">Computadores no asignados</a></li>
        <li><a class="dropdown-item" @click="filterTypeAssigned('False','2')">Telefonos no asignados</a></li>
        <li><a class="dropdown-item" @click="filterTypeAssigned('False','3')">Monitores no asignados</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item"  @click="filterType('1')">Todos los computadores</a></li>
        <li><a class="dropdown-item" @click="filterType('2')">Todos los telefonos</a></li>
        <li><a class="dropdown-item" @click="filterType('3')">Todos los monitores</a></li>
        
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" @click="refreshData()">Todos los dipositivos</a></li>
      </ul>
    </div>
    <br>

  </div>
  <div class="container" style="text-align:center;"> 
  <table class="table table_hover" border="0" style="margin: 0 auto;">  
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Modelo</th>
      <th scope="col">Tipo</th>
      <th scope="col">Garantia</th>
      <th scope="col">Numero</th>
      <th scope="col">Estatus</th>
      <th scope="col">Asignado?</th>
      <th scope="col">Opciones</th>
    </tr>
  </thead>
  <tbody v-for="device in Devices.results" :key="device.id">
    <tr>
      <th scope="row">{{ device.id_device }}</th>
      <td>{{ device.Model }}</td>
      <td v-if="device.id_type==1"> Notebook</td>
      <td v-else-if="device.id_type==2"> Telefono</td>
      <td v-else> Pantalla</td>
      <td>{{ device.Waranty }}</td>
      <td>{{ device.Number }}</td>
      <td>{{ device.Status }}</td>  
      <td v-if="device.Assigned">Si</td>
      <td v-else>No</td>
      <td>
        <div class="btn-group" role="group" aria-label="Basic example">
          <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleMod" data-bs-whatever="@getbootstrap" @click="getData(device.id_device)">Editar</button>
          
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
                  <label for="id_device" class="col-form-label">Numero de serie:</label>
                  <input type="text" class="form-control" id="id_device" v-model="devi.id_device">
                </div>
                <div class="mb-3">
                  <label for="id_type" class="col-form-label">Tipo:</label>
                  <select class="form-select" id="id_type" v-model="devi.id_type">
                    <option value="1">Notebook</option>
                    <option value="2">Telefono</option>
                    <option value="3">Monitor</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="Modelo" class="col-form-label">Modelo:</label>
                  <input type="text" class="form-control" id="Modelo" v-model="devi.Model">
                </div>
                <div class="mb-3">
                  <label for="Waranty" class="col-form-label">Garantia:</label>
                  <input type="date" class="form-control" id="Waranty" v-model="devi.Waranty">
                </div>
                <div class="mb-3">
                  <label for="Number" class="col-form-label">Numero:</label>
                  <input type="number" class="form-control" id="Number" v-model="devi.Number">
                </div>
                <div class="mb-3">
                  <label for="Status" class="col-form-label">Estatus:</label>
                  <select class="form-select" id="Status" v-model="devi.Status">
                    <option value="Normal">Normal</option>
                    <option value="Danado">Dañado</option>
                    <option value="Alto">Alto uso</option>
                    <option value="Operativo">No operativo</option>
                    <option value="No">No especifica</option>
                  </select>
                </div>
                <div class="mb-3">
                  <label for="Asigned" class="col-form-label">Asignado?:</label>
                  <select class="form-select" id="Asigned" v-model="devi.Assigned">
                    <option value="true">Si</option>
                    <option value="false">No</option>
                  </select>
                </div>
              </div>
              <div class="mb-3">
                  <label for="last_change" class="col-form-label">Last_change:</label>
                  <select class="form-select" id="last_change" v-model="devi.last_change">
                    <option value="1">Admin</option>
                  </select>
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
    <li  v-if="Devices.count" scope="row" class="page-item" v-for="page in Math.ceil(Devices.count/50)">
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
      id_device:'',
      id_type:0,
      Model:'',
      Waranty:null,
      Number:null,
      Status:'',
      Assigned:false,
      last_change:1,
      Devices: [],
      devi:[],
      serialnumber:''
    };

  },
  methods:{
    refreshData(){
          axios.get('http://127.0.0.1:8000/api/api/device/')
          .then((response) => {
            this.Devices = response.data;});
        },
    async filterSn(id_device){
      await axios.get('http://127.0.0.1:8000/api/api/device/?id_device='+id_device)
          .then((response) => {
            this.Devices = response.data;});
    },

    async filterAssigned(asig){
      await axios.get('http://127.0.0.1:8000/api/api/device/?Assigned='+asig)
          .then((response) => {
            this.Devices = response.data;});
    },
    async filterTypeAssigned(assig,type){
      await axios.get('http://127.0.0.1:8000/api/api/device/?Assigned='+assig+'&id_type='+type)
          .then((response) => {
            this.Devices = response.data;});
    },

    async filterType(type){
      await axios.get('http://127.0.0.1:8000/api/api/device/?id_type='+type)
          .then((response) => {
            this.Devices = response.data;});
    },

    async getData(id){
          await axios.get('http://127.0.0.1:8000/api/api/device/'+id)
          .then(response => {
            this.devi = response.data;});
        },
    async getPage(page){
          await axios.get('http://127.0.0.1:8000/api/api/device/?page='+page)
          .then(response => {
            this.Devices = response.data;
            window.scrollTo({top:0,behavior:'smooth'});
          });

        },
    async sendData(){
          const datatosend ={
            id_device:this.id_device,
            id_type:this.id_type,
            Model:this.Model,
            Waranty:this.Waranty,
            Number:this.Number,
            Status:this.Status,
            Assigned:this.Assigned,
            last_change:this.last_change
          };
          await axios.post('http://127.0.0.1:8000/api/api/device/',datatosend)
          .then(response => {console.log(response.data);window.location.reload()
          }).catch(error => {console.error('Error en el envio', error);
            alert("Error en el envio ") ;
        });
        },
    async deleteData(id){
          await axios.delete('http://127.0.0.1:8000/api/api/device/'+id)
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
            id_device:this.devi.id_device,
            id_type:this.devi.id_type,
            Model:this.devi.Model,
            Waranty:this.devi.Waranty,
            Number:this.devi.Number,
            Status:this.devi.Status,
            Assigned:this.devi.Assigned,
            last_change:this.devi.last_change
          };
          await axios.put('http://127.0.0.1:8000/api/api/device/'+this.devi.id_device+'/',modData)
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