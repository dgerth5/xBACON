#### Read Data ####

library(readr)
statcast18 = read_csv("C:/Users/david/PycharmProjects/pythonProject/statcast18.csv")
statcast19 = read_csv("C:/Users/david/PycharmProjects/pythonProject/statcast19.csv")
statcast20 = read_csv("C:/Users/david/PycharmProjects/pythonProject/statcast20.csv")
statcast21 = read_csv("C:/Users/david/PycharmProjects/pythonProject/statcast21.csv")
statcast22 = read_csv("C:/Users/david/PycharmProjects/pythonProject/statcast22.csv")

statcast_full = rbind(statcast18,statcast19,statcast20,statcast21,statcast22) 

unique(statcast22$events)

#### Modify Table ####

library(lubridate)
statcast = statcast_full %>%
  mutate(month = month(game_date),
         year = year(game_date),
         pitch_team = if_else(inning_topbot == "Top",away_team,home_team)) %>%
  filter(description == "hit_into_play") %>%
  filter(events != "sac_bunt" & events != "sac_fly" & events != "sac_bunt_double_play" & events != "catcher_interf") %>%
  mutate(hit = if_else(events == "single" | events == "double" | events == "triple" | events == "home_run", 1, 0)) %>%
  select(hit, events, batter, pitcher, zone, stand, p_throws, home_team, pitch_team, strikes, month, game_year, launch_speed, launch_angle)

statcast$batter = as.factor(statcast$batter)
statcast$pitcher = as.factor(statcast$pitch_team)
statcast$p_throws = as.factor(statcast$p_throws)
statcast$stand = as.factor(statcast$stand)
statcast$zone = as.factor(statcast$zone)
statcast$home_team = as.factor(statcast$home_team)
statcast$pitch_team = as.factor(statcast$pitch_team)
statcast$game_year = as.factor(statcast$game_year)
statcast$month = as.factor(statcast$month)
