<template>
<br>
<div class="container">
  <div class="input-group">

  <button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Agregar +</button>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">Nuevo Empleado/dispositivo:</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <form>
                <div class="input-group mb-3">
                <div class="mb-3">
                  <label for="id_employees" class="col-form-label">Rut del empleado:</label>
                  <input type="number" class="form-control" id="id_employees" v-model="id_employees">
                </div>
                <div class="mb-3">
                  <label for="id_device" class="col-form-label">Numero de serie:</label>
                  <input type="text" class="form-control" id="id_device" v-model="id_device">
                </div>
                <div class="mb-3">
                  <label for="Assig_date" class="col-form-label">Dia de asignacion</label>
                  <input type="date" class="form-control" id="Assig_date" v-model="Assig_date">
                </div>
                <div class="mb-3">
                  <label for="Finn_date" class="col-form-label">Fecha de finalizacion:</label>
                  <input type="date" class="form-control" id="Finn_date" v-model="Fin_date">
                </div>
                <div class="mb-3">
                  <label for="last_change" class="col-form-label">Admin:</label>
                  <select class="form-select" id="last_change" v-model="last_change">
                    <option value="1">Admin</option>
                  </select>
                </div>
              </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                  <button type="button" class="btn btn-success"  @click="sendData()">Agregar</button>
                </div>
              </form>
            </div>
          </div>
        </div>  
      </div>

      <input type="text" class="form-control" aria-label="Text input with segmented dropdown button" placeholder="Ingrese el Rut . . ." v-model="nombre">
      <button type="button" class="btn btn-outline-secondary btn-lg" @click="employefilter(nombre)">Buscar</button>
      <input type="text" class="form-control" aria-label="Text input with segmented dropdown button" placeholder="Ingrese el numero de serie . . ." v-model="sn">
      <button type="button" class="btn btn-outline-secondary btn-lg" @click="devicefilter(sn)">Buscar</button>
      <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
        <span class="visually-hidden">Toggle Dropdown</span>
      </button>
      <ul class="dropdown-menu dropdown-menu-end">
        <li><a class="dropdown-item" @click="nulfilter()">Todos los asignados</a></li>
        <li><a class="dropdown-item" @click="notnulfilter()">Todos los finalizados</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" @click="refreshData()">Todas las asignaciones</a></li>
      </ul>
    </div>
    <br>

  </div>
  <div class="container" style="text-align:center;"> 
  <table class="table table_hover" border="0" style="margin: 0 auto;">  
  <thead>
    <tr>
      <th scope="col">Rut</th>
      <th scope="col">Nombre</th>
      <th scope="col">Serial/Number</th>
      <th scope="col">Tipo</th>
      <th scope="col">Fecha/Asignacion</th>
      <th scope="col">Fecha/Finalizacion</th>
      <th scope="col">Opciones</th>
    </tr>
  </thead>
  <tbody v-for="employedevice in employeedevices.results" :key="employedevice.id">
    <tr>
      <th scope="row">{{ employedevice.id_employees  }}</th>
      <td>{{ employedevice.nombre }}</td>
      <td>{{ employedevice.id_device }}</td>
      <td>{{ employedevice.tipo }}</td>
      <td>{{ employedevice.Assig_date }}</td>
      <td>{{ employedevice.Fin_date }}</td>
      <td>
        <div class="btn-group" role="group" aria-label="Basic example">          
          <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleMod" data-bs-whatever="@getbootstrap" @click="getData(employedevice.id_ed)">Editar</button>
          
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
                  <label for="id_employees" class="col-form-label">Rut del empleado:</label>
                  <input type="number" class="form-control" id="id_employees" v-model="ende.id_employees">
                </div>
                <div class="mb-3">
                  <label for="id_device" class="col-form-label">Numero de serie:</label>
                  <input type="text" class="form-control" id="id_device" v-model="ende.id_device">
                </div>
                <div class="mb-3">
                  <label for="Assig_date" class="col-form-label">Dia de asignacion</label>
                  <input type="date" class="form-control" id="Assig_date" v-model="ende.Assig_date">
                </div>
                <div class="mb-3">
                  <label for="Finn_date" class="col-form-label">Fecha de finalizacion:</label>
                  <input type="date" class="form-control" id="Finn_date" v-model="ende.Fin_date">
                </div>
                <div class="mb-3">
                  <label for="last_change" class="col-form-label">Admin:</label>
                  <select class="form-select" id="last_change" v-model="ende.last_change">
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

          <button type="button" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#exampleModa" @click="getData(employedevice.id_ed)">Eliminar</button>
          <div class="modal fade" id="exampleModa" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Eliminar Empleado/dispositivo</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <label>Esta seguro que quiere continuar con la eliminacion?</label>
              </div>
              <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        <button type="button"  class="btn btn-danger" @click="deleteData(ende.id_ed)">Eliminar</button>
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
    <li  v-if="employeedevices.count" scope="row" class="page-item" v-for="page in Math.ceil(employeedevices.count/50)">
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
      id_ed:0,
      id_employees:0,
      id_device:'',
      Assig_date:'',
      Fin_date: null,
      last_change:1,
      nombre:"",
      employeedevices: [],
      ende: [],
      devices:[],
      nombre:'',
      sn:''
    };
  },
  methods:{
    refreshData(){
          axios.get('http://127.0.0.1:8000/api/api/employedevice/')
          .then((response) => {
            this.employeedevices = response.data;});
        },

    async employefilter(id){
         await  axios.get('http://127.0.0.1:8000/api/api/employedevice/?id_employees='+id)
          .then((response) => {
            this.employeedevices = response.data;});
    },
    async devicefilter(id){
         await axios.get('http://127.0.0.1:8000/api/api/employedevice/?id_device='+id)
          .then((response) => {
            this.employeedevices = response.data;});
    },
    async nulfilter(){
      await axios.get('http://127.0.0.1:8000/api/api/employedevice/?Fin_date')
      .then((response) => {
            this.employeedevices = response.data;});

    },
    async notnulfilter(){
      await axios.get('http://127.0.0.1:8000/api/api/employedevice/?Fin_date=false')
      .then((response) => {
            this.employeedevices = response.data;});
    },
    async sendData() {
    const datatosend = {
                    id_ed: this.id_ed,
                    id_employees: this.id_employees,
                    id_device: this.id_device,
                    Assig_date: this.Assig_date,
                    Fin_date: this.Fin_date,
                    last_change: this.last_change
                }; 
        await axios.get('http://127.0.0.1:8000/api/api/employedevice/?id_device='+this.id_device+'&Fin_date')
        .then(response => {
            if (response.data.count > 0) {
                console.log('Ya existe un elemento con el mismo id_device y Fin_date igual a null. No se puede realizar la solicitud POST.');
            } else {       
                axios.post('http://127.0.0.1:8000/api/api/employedevice/', datatosend)
                    .then(response => {
                        console.log(response.data);
                        window.location.reload();
                    })
                    .catch(error => {
                        console.error('Error en el envio', error);
                    alert("Error en el envio ") ;
                    });
                    if(this.Fin_date == null){
                      axios.patch('http://127.0.0.1:8000/api/api/device/'+this.id_device+'/',{Assigned: true})
                    }
            }
        })
        .catch(error => {
            console.error('Error al realizar la solicitud GET para verificar la existencia de otro elemento con el mismo id_device y Fin_date igual a null.', error); 
        });
        },
     async getData(id){
          await axios.get('http://127.0.0.1:8000/api/api/employedevice/'+id)
          .then(response => {
            this.ende = response.data;});
        },
      async getPage(page){
          await axios.get('http://127.0.0.1:8000/api/api/employedevice/?page='+page)
          .then(response => {
            this.employeedevices = response.data;
            window.scrollTo({top:0,behavior:'smooth'});
          });

        },

    async deleteData(id){
          await axios.delete('http://127.0.0.1:8000/api/api/employedevice/'+id)
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
            id_employees:this.ende.id_employees,
            id_device:this.ende.id_device,
            Assig_date:this.ende.Assig_date,
            Fin_date:this.ende.Fin_date,
            last_change:this.ende.last_change
          };
          
          if(this.ende.Fin_date!=null){
            axios.patch('http://127.0.0.1:8000/api/api/device/'+this.ende.id_device+'/',{Assigned: false})
            .then(response => {console.log(response.data);window.location.reload()
          }).catch(error => {console.error('Error en el envio', error); 
          }); 
          };

          await axios.put('http://127.0.0.1:8000/api/api/employedevice/'+this.ende.id_ed+'/',modData)
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