import { api } from "boot/axios";

/*
 * Добавьте перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => {
    return Promise.reject(error);
  }
);

export const links = {
  // Новая ссылка
  async add_new_link(data) {
    try {
      let res = await api.post(`/links/add`, data);
      return res.status;
    } catch (error) {
      console.log(error);
      return false;
    }
  },
  /**
   * Получение списка
   * @returns
   */
  async get_links(limit, offset) {
    try {
      let res = await api.get(`/pars/links?limit=${limit}&offset=${offset}`);
      return res.data;
    } catch (error) {
      console.log(error.message);
      return error.code;
    }
  },

  async get_statuts() {
    try {
      let res = await api.get(`/pars/links-status`);
      return res.data.data;
    } catch (error) {
      console.log(error.message);
      return false;
    }
  },
  async edit_link(id_link, id_status) {
    try {
      let data = {
        status_id: id_status,
      };
      let res = await api.put(`/pars/links/edit/${id_link}`, data);
    } catch (error) {
      console.log(error.message);
      return false;
    }
  },
};

export const homes = {
  // Новая ссылка
  async add_new_home(data) {
    try {
      let res = await api.post(`/pars/add`, data);
      return res.status;
    } catch (error) {
      console.log(error);
      return false;
    }
  },
  /* CRUD для Региона */
  async add_new_region(data) {
    try {
      let res = await api.post(`/realty/regions`, data);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async get_list_regions() {
    try {
      let res = await api.get(`/realty/regions?skip=0&limit=1000`);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  /* Районы */
  async get_list_districts(region_id) {
    try {
      let res = await api.get(
        `/realty/districts/${region_id}?skip=0&limit=1000`
      );
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async add_new_district(data) {
    try {
      let res = await api.post(`/realty/district`, data);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  /* Типы поселений */
  async add_new_settlement_type(data) {
    try {
      let res = await api.post(`/realty/settlement-type`, data);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async get_list_settlement_types() {
    try {
      let res = await api.get(`/realty/settlement-type?skip=0&limit=1000`);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  /* Поселения */
  async get_list_settlements(region_id, district_id, settlement_type_id) {
    try {
      let res = await api.get(
        `/realty/settlements/${region_id}/${district_id}/${settlement_type_id}?skip=0&limit=1000`
      );
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async add_new_settlement(data) {
    try {
      let res = await api.post(`/realty/settlement`, data);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },

  /* Объявления */
  async get_list_homes() {
    try {
      let res = await api.get(`/realty/houses?skip=0&limit=1000`);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async get_home(id) {
    try {
      let res = await api.get(`/realty/house/${id}`);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async find_home(uid) {
    try {
      let res = await api.get(`/realty/find-house/${uid}`);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async find_link(id) {
    try {
      let res = await api.get(`/pars/link/find/${id}`);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
  async add_new_home(data) {
    try {
      let res = await api.post(`/realty/home/`, data);
      return res.data;
    } catch (error) {
      if (error.response) {
        return error.response.data.detail;
      }
    }
  },
};
