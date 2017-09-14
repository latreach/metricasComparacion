setwd("~/local/Alexis")

library(magrittr)
c("dplyr", "tidyr", "lubridate", "Rfacebook", "ggplot2",
  "googlesheets", "data.table") %>%
  sapply(require,character.only=T)


fb_oauth <- fbOAuth(app_id="1611650985792093",
                    app_secret="85db5a49077d074e84b5ce0a19659893",
                    extended_permissions = TRUE)
save(fb_oauth, file="fb_oauth")
load("~/fb_oauth")

tok <- "EAAW5ybyCkl0BAKqdSjwZAXlNcnW3aGgnNf13XWq5iBeUbaTRW4AMjYqwK6wncGHeQbeXOBEpD8ncjsAk7nY9NZBRkUmhQjeDfmuF2OYVkRllLGfskZCTpm1Iby4WBOgMSomtQSOipNGEb9f2kZBZCXFEk8jZBuE1V6j2GZBniPZBNAZDZD"


# -------- SEAT.Mexico

SEATMexicoID <- 113144262054871

SEATMexico <- getPage(SEATMexicoID,token=tok,
                    since="2017-07-01",until="2017-09-01",
                    n=10000,reactions=T,feed = T)


# readLines("https://graph.facebook.com/v2.10/me/insights/page_impressions?access_token=EAACEdEose0cBAH8lSuGv1FLMZAhMFO568xgZBIKMGdjBhQJFF1jKBp1KIUZC87w2mWfompry1ll5M7fdjdoJZBru1gFzG76a44lJjTpn6oEQ82HuJkIfCOPybs9UMRxUbUZBJSPvCGb7YlfKrDWi0ZAMyZBBuZA9MlUHPb1DFcFFuHGSwJzApsVoPAScdOXDi6wZD") %>% 
#   fromJSON()


SEATMexico %>%
  filter(from_id == "113144262054871") %>%
  mutate(mes = months(as.Date(gsub("T\\S+", "", created_time)))) %>%
  filter(mes == "agosto") %>% 
  select(likes_count, comments_count, shares_count,
         love_count, haha_count, wow_count, sad_count, angry_count) %>% 
  rowSums() %>% sum


347+70+112+387+439+356+330+381+184+1563+1365+1423+710+372