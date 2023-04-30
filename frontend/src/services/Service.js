import { useNavigationsStore } from "stores/navigations";
import { useMeta } from "quasar";
import { api } from "boot/axios";

/*
 * Добавьте перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => Promise.reject(error)
);

/**
 * Добавление элнментов в модуль Хлебных крошек
 * @param {String} add_routes объект массивов [{ path: "/to_route" , meta: {title: "This Title Page"}}]
 * @param {String} current_page_title заголовок текущей страницы
 * @param {Boolean} reset перезапись всего пути
 */
export const setBreadscrumbs = (
  add_routes,
  current_page_title,
  reset = false
) => {
  const navigations = useNavigationsStore();
  navigations.current_title = current_page_title;
  if (!reset) {
    navigations.breadscrumbs = [...navigations.breadscrumbs, ...add_routes];
  } else {
    navigations.breadscrumbs = add_routes;
  }
};

/**
 *  Установить Мета заголовок
 * @param {String} srt_title
 * @param {String} prev_str
 */
export const setMetaTitle = (srt_title, prev_str = " : Усадьба Мечты") => {
  useMeta(() => {
    return {
      title: srt_title + prev_str,
    };
  });
};

export const serviceNode = {
  async get_node(fullPath){
    try {
      let res = await api.get(`/node/${fullPath}`);
      return res.data;
    } catch (error) {
      console.log(error);
    }
  },
};
