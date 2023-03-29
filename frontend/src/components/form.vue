<script setup>
import axios from 'axios'
</script>
<template>
    	<div id="loading" v-if="loading">
	</div>
    <div v-else></div>
        <main class="max-h-fit p-1 pt-40 flex items-start place-content-center bg-slate-200 dark:bg-slate-700 min-h-screen">
    <div class="max-w-[1000px] shadow-lg p-6 rounded-lg bg-slate-100 dark:bg-gray-700 place-content-center">
      <div class="flex items-start md:items-center mb-4 place-content-center">
        <form @submit="submit" enctype="multipart/form-data" ref="form">
            <div>
            <input type="text" id="first_name" class="bg-slate-100 border border-gray-300 text-gray-900 text-md rounded-md focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Column Names" v-model="cname">
        </div><br>
        <div>
<input ref="file" class="block w-full text-md text-gray-900 border border-gray-300 rounded-md cursor-pointer bg-slate-100 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input" type="file" v-on:change="file">
            </div><br>
            <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-sm sm:w-sm px-5 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Submit    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
  <path fill-rule="evenodd" d="M3 10a.75.75 0 01.75-.75h10.638L10.23 5.29a.75.75 0 111.04-1.08l5.5 5.25a.75.75 0 010 1.08l-5.5 5.25a.75.75 0 11-1.04-1.08l4.158-3.96H3.75A.75.75 0 013 10z" clip-rule="evenodd" />
</svg>

            </button>
        </form>
</div>
    </div>
  </main>
</template>
<script>
export default {
    name : 'form1',
    data() {
    return {
      cname: 'A,B,C',
      loading: false
      }
    },
    methods:{
        submit(e)
        {
            e.preventDefault();
            this.loading = true;
            this.file = this.$refs.file.files[0];
            if(!this.cname || !this.file){
                this.loading = false;
                this.$swal({title: 'All fields are required',
                    text: "",
                    icon: 'info',
                    timer: 1500,
                    showConfirmButton: false,
                    timerProgressBar: true});
            } else if(this.cname.length < 7){
                this.loading = false;
                this.$swal({title: 'Minimum 4 columns are required',
                    text: "",
                    icon: 'info',
                    timer: 1500,
                    showConfirmButton: false,
                    timerProgressBar: true});
            } else if (!this.file.type.includes('spreadsheetml') && !this.file.type.includes('sheet')){
                this.$refs.file.value = null;
                this.loading = false;
                this.$swal({title: 'Only excel files are allowed',
                    text: "",
                    icon: 'info',
                    timer: 1500,
                    showConfirmButton: false,
                    timerProgressBar: true});
            } else{
                this.$swal({
                    title: 'Are you sure?',
                    text: "Are the column names correct?",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Yes!'
                    }).then((result) => {
                    if (result.isConfirmed) {
                        let formData = new FormData();
                        formData.append('file', this.file);
                        formData.append('columns', this.cname);
                        axios.defaults.headers = {
                        'Cache-Control': 'no-cache',
                        'Pragma': 'no-cache'
                        };
                        axios.post('/backend/',formData, {
                                    responseType: 'arraybuffer',
                                    headers: {
                                        'Content-Type': 'multipart/form-data'
                                    }
                                })
                                .then((response) => {
                                    const url = window.URL.createObjectURL(new Blob([response.data], {type: 'application/x-zip-compressed'}));
                                    const link = document.createElement('a');
                                    link.href = url;
                                    link.setAttribute('download', 'output.zip');
                                    document.body.appendChild(link);
                                    link.click();
                                    this.loading = false;
                                    link.remove();
                                    this.$swal({title: 'Done!',
                                                text: "",
                                                icon: 'success',
                                                timer: 2000,
                                                showConfirmButton: false,
                                                timerProgressBar: true});
                                    this.$refs.form.reset();
                                    this.cname = 'A,B,C';
                                })
                                .catch(error => {
                                    if (error.response){
                                        if (error.response.status === 400){
                                            this.loading = false;
                                            this.$swal({title: 'Only excel files are allowed',
                                                        text: "",
                                                        icon: 'info',
                                                        timer: 1500,
                                                        showConfirmButton: false,
                                                        timerProgressBar: true});
                                        } else{
                                            this.loading = false;
                                            this.$swal({title: 'Internal Server Error',
                                                        text: "",
                                                        icon: 'info',
                                                        timer: 1500,
                                                        showConfirmButton: false,
                                                        timerProgressBar: true});
                                        }
                                    }                            
                                });
                    }else if (
                            /* Read more about handling dismissals below */
                            result.dismiss === Swal.DismissReason.cancel
                        ) {
                            this.loading = false;
                        }
                    })
            }
        }
    }
}
</script>

<style>
    		#loading{
			position: fixed;
			width: 100%;
			height: 100vh;
			background: rgba(78, 78, 78, 0.596) url('/loader.svg') no-repeat center;
			z-index: 999;
			background-size: 100px 100px;
		}
</style>