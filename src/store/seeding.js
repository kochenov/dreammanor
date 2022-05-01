import axios from "axios";

export default {
  state: {
    vegetableId: 1, // Данные текущего овоща
    vegetables: [], // список овощей
    errorDataApi: false, // Если данные не прогрузились
  },
  getters: {
    // Список сортов текущего овоща
    getSorts: (state) => {
      return { ...state.vegetables.find((s) => s.id == state.vegetableId) }
        .sorts;

      //return [];
    },
    getVegetable: (state) => {
      return { ...state.vegetables.find((s) => s.id == state.vegetableId) };
    },
  },
  mutations: {
    // Массив списка сортов текущего овоща
    setVegetables: (state, vegetables) => {
      state.vegetables = vegetables;
    },
    // Установка выбранного овоща
    setVegetableId: (state, id) => {
      state.vegetableId = id;
    },
    // Установка выбранного овоща
    setErrorApi: (state, status) => {
      state.errorDataApi = status;
    },
  },
  actions: {
    loadVegetables({ commit }) {
      axios({
        method: "GET",
        url: `http://127.0.0.1:8000/api/V1/vegetable`,
        //params: {},
        //data: {},
        headers: {
          "Content-type": "application/json; charset=UTF-8",
        },
      })
        .then((response) => {
          commit("setVegetables", response.data.data);
        })
        .catch((error) => {
          commit("setErrorApi", true); // Показать ошибку получения данных
          console.log(error);
        })
        .finally(() => {
          //console.log(state.errorDataApi);
          //commit("setErrorApi", false);
        });
    },
  },
};
