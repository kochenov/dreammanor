import { defineStore } from "pinia";
import { links, homes } from "./service";
import { Notify } from "quasar";

export const useEstateStore = defineStore("estateStore", {
  state: () => ({
    links: null, // список новостей
    status_list: null,
    loading: false, // Пока труе, идёт загрузка
    count_links: 0, // колисечтво постов
    limit: 10, // Количество постов
    regions: null,
    districts: null,
    settlements: null,
    settlement_types: null,
    homes: null,
    home_item: null,
    error: null,
  }),

  actions: {
    /**
     * Загрузка списка
     * @param {*}
     */
    async getLinks(offset = 0) {
      try {
        let data = await links.get_links(this.limit, offset);
        if (data == "ERR_NETWORK") {
          Notify.create({
            message: "Нет соединения с интернетом!",
            color: "red",
          });
          this.error = ["Ошибка данных"];
        }
        this.status_list = await links.get_statuts();
        this.links = data.data;
      } catch (error) {
        console.log(error);
        this.error = [error];
      }
    },

    async editLinks(id_link, id_status) {
      try {
        await links.edit_link(id_link, id_status);
      } catch (error) {
        console.log(error);
      }
    },
    /* Регионы  */
    async getRegions() {
      try {
        let data = await homes.get_list_regions();
        if (data == "ERR_NETWORK") {
          Notify.create({
            message: "Нет соединения с интернетом!",
            color: "red",
          });
          this.error = ["Ошибка данных"];
        }
        this.regions = data.data;
      } catch (error) {
        console.log(error);
        this.error = [error];
      }
    },
    async addNewRegion(data) {
      try {
        let res = await homes.add_new_region(data);
        this.error = res.status == "error" ? "error" : null;
        Notify.create({
          message: res.message,
          color: res.status == "error" ? "red" : "green",
        });
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    /* Районы  */
    async getDistricts(region_id) {
      try {
        let res = await homes.get_list_districts(region_id);
        this.error = res.status == "error" ? "error" : null;
        if (res.status == "error") {
          Notify.create({
            message: res.message,
            color: res.status == "error" ? "red" : "green",
          });
        }
        this.districts = res.data;
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    async addNewDistrict(data) {
      try {
        let res = await homes.add_new_district(data);
        this.error = res.status == "error" ? "error" : null;
        Notify.create({
          message: res.message,
          color: res.status == "error" ? "red" : "green",
        });
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    /* Типы поселений */
    async getSettlementTypes() {
      try {
        let data = await homes.get_list_settlement_types();
        this.settlement_types = data.data;
      } catch (error) {
        console.log(error);
        this.error = [error];
      }
    },
    async addNewSettlementType(data) {
      try {
        let res = await homes.add_new_settlement_type(data);
        this.error = res.status == "error" ? "error" : null;
        Notify.create({
          message: res.message,
          color: res.status == "error" ? "red" : "green",
        });
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    /* Поселения */
    async getSettlements(region_id, district_id, settlement_type_id) {
      try {
        let res = await homes.get_list_settlements(
          region_id,
          district_id,
          settlement_type_id
        );
        this.error = res.status == "error" ? "error" : null;
        if (res.status == "error") {
          Notify.create({
            message: res.message,
            color: res.status == "error" ? "red" : "green",
          });
        }
        this.settlements = res.data;
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    async addNewSettlement(data) {
      try {
        let res = await homes.add_new_settlement(data);
        this.error = res.status == "error" ? "error" : null;
        Notify.create({
          message: res.message,
          color: res.status == "error" ? "red" : "green",
        });
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },

    /* Объявления */
    async getHomes() {
      try {
        let res = await homes.get_list_homes();

        this.error = res.status == "error" ? "error" : null;

        if (res.status == "info") {
          Notify.create({
            message: res.message,
            color: "info",
          });
        }
        if (res.status == "error") {
          Notify.create({
            message: res.message,
            color: res.status == "error" ? "red" : "green",
          });
        }
        this.homes = res.data;
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    async getHome(id_home) {
      try {
        this.home_item = null;
        this.loading = true;

        let res = await homes.get_home(id_home);

        this.error = res.status == "error" ? "error" : null;
        if (res.status == "error") {
          Notify.create({
            message: res.message,
            color: res.status == "error" ? "red" : "green",
          });
        }
        this.home_item = res.data;
        this.loading = false;
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    async addNewHome(data) {
      try {
        let res = await homes.add_new_home(data);
        this.error = res.status == "error" ? "error" : null;

        Notify.create({
          message: res.message,
          color: res.status == "error" ? "red" : "green",
        });

        return res.status;
      } catch (error) {
        if (error.response) {
          return error.response.data.detail;
        }
      }
    },
    async findHome(uid) {
      try {
        let res = await homes.find_home(uid);

        this.error = res.status == "error" ? "error" : null;
        if (res.status == "error") {
          Notify.create({
            message: res.message,
            color: res.status == "error" ? "red" : "green",
          });
        }
        return res.data;
      } catch (error) {
        if (error.response) {
          return null;
        }
      }
    },
    async findLink(id) {
      try {
        let res = await homes.find_link(id);

        this.error = res.status == "error" ? "error" : null;
        if (res.status == "error") {
          Notify.create({
            message: res.message,
            color: res.status == "error" ? "red" : "green",
          });
        }
        return res.data;
      } catch (error) {
        if (error.response) {
          return null;
        }
      }
    },
  },
  getters: {},
});
