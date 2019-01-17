# 9. Use insert() to add one new university to the beginning of your list.


# Creating list of Universities
univerities_i_wish_to_attend = ["Harvard", "Stanford", "Princeton", "MIT", "CalTech", "Berkeley"]

# University I cannot attend
university_i_cannot_attend = "Princeton"

# Remove university I cannot attend
univerities_i_wish_to_attend.remove(university_i_cannot_attend)

# Create new university
new_university = "University of Lagos"

# Add new university to my list
univerities_i_wish_to_attend.append(new_university)

# Using insert to add Tsinghua University at beginning
univerities_i_wish_to_attend.insert(0, "Tsinghua University")