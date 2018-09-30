<template>
<b-container fluid class='bv-example-row bv-example-row-flex-cols'>
    <index-page></index-page>
</b-container>
</template>

<script>
import IndexPage from '@/components/IndexPage';
export default {
    components: {
        IndexPage
    }
}
</script>

<style>
.container-fluid {
    height: 100%;
}
.asd {
    margin-top: auto;
    margin-bottom: auto;
}
.test-div {
    /* display: block; */
    background: rgba(255, 255
    , 255, 0.5);
    height: 50vh;
    border-radius: 8px;
    /* filter: blur(10px); */
    /* -webkit-filter: blur(10px); */
}
/* .test-div{
   top: 200px;
   height: 50%;
   min-height: 50%;
   margin-bottom: 20px;
   background: rgba(255, 255, 255, 0.4);
   z-index:1010;
   -webkit-filter: blur(8px);
   -moz-filter: blur(8px);
   -o-filter: blur(8px);
   -ms-filter: blur(8px);
   filter: blur(8px);
} */

</style>
