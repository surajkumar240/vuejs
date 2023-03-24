<script setup>
import { useDark, useToggle } from "@vueuse/core";
import form1 from './form.vue'
const isDark = useDark();
const toggleDark = useToggle(isDark);
</script>
<template>
<nav class="shadow-md bg-slate-200 px-2 sm:px-4 py-2.5 dark:bg-slate-700 fixed w-full z-20 top-0 left-0 border-b border-gray-200 dark:border-gray-600">
  <div class="container flex flex-wrap items-center justify-between mx-auto">
  <a href="#" class="flex items-center">
      <span class="pl-2.5 self-center text-xl font-semibold whitespace-nowrap dark:text-white">Excel2CSV</span>
  </a>
  <div class="flex md:order-2">
      <button type="button" aria-labelledby="toggleBtn" class="transition-transform hover:-translate-y-1 text-black focus:outline-none font-medium rounded-full text-sm px-5 py-2.5 text-center pr-2.5 md:mr-0 dark:text-white" @click="toggleDark()"><span v-if="isDark"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
</svg>
</span><span v-else><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
  <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.718 9.718 0 0118 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 003 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 009.002-5.998z" />
</svg>
</span></button>
  </div>

  </div>
</nav>
    <form1></form1>
</template>
export default navBar