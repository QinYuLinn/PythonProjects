import math
ball_ridus=2.625
ratio_from_arch_to_degree=180.0/math.pi
table_legth=356.9
table_width=177.8
obball_targetball_distance=table_width/8.0
table_half_width=table_width/2.0
ball_blue_distance_buttom=table_legth/2.0
ball_pink_distance_top=table_legth/4.0
ball_black_distance_top=32.4
table_break_line_distance_buttom=73.7
table_ridus_break_cicle=29.2
temp=0.0
my_fix_parameter=2*ball_ridus/obball_targetball_distance
my_fix_parameter_quater=2*ball_ridus/table_width*4.0
def my_fixed_kappa(jiaodu,canshu,zhuanhuanxishu):
    return 2.0*math.sin(jiaodu/zhuanhuanxishu)/(1.0-canshu*math.cos(jiaodu/zhuanhuanxishu))
angle_black=[]
angle_black.append(math.atan2(ball_black_distance_top,table_half_width)*2.0*ratio_from_arch_to_degree)#黑球第一个角度
angle_black.append(math.atan2(ball_black_distance_top,table_half_width)*ratio_from_arch_to_degree)#黑球第二个角度
angle_black.append(0)#黑球第三个角度
temp=(math.atan2(ball_pink_distance_top-ball_black_distance_top,table_half_width)-math.atan2(ball_black_distance_top,table_half_width))*ratio_from_arch_to_degree
angle_black.append(temp)#黑球第四个角度
temp=0.0
temp=(math.atan2(table_legth*3.0/8.0-ball_black_distance_top,table_half_width)-math.atan2(ball_black_distance_top,table_half_width))*ratio_from_arch_to_degree
angle_black.append(temp)#黑球第五个角度
temp=(math.atan2(ball_blue_distance_buttom-ball_black_distance_top,table_half_width)-math.atan2(ball_black_distance_top,table_half_width))*ratio_from_arch_to_degree
angle_black.append(temp)#黑球第六个角度

angle_pink=[]
#angle_pink.append(math.atan2(table_legth/4.0,table_half_width)*ratio_from_arch_to_degree)#粉球第1个角度
temp=(math.atan2(table_legth/4.0,table_half_width)-math.atan2(table_legth/8.0,table_half_width))*ratio_from_arch_to_degree
angle_pink.append(temp)#粉球第2个角度
angle_pink.append(0)#粉球第3个角度
temp=(math.atan2(table_legth*4.0/8.0-table_break_line_distance_buttom/2.0,table_half_width)-math.atan2(table_legth/4.0,table_half_width))*ratio_from_arch_to_degree
angle_pink.append(temp)#粉球第4个角度

temp=(math.atan2(table_legth*3.0/4.0-table_break_line_distance_buttom,table_half_width)-math.atan2(table_legth/4.0,table_half_width))*ratio_from_arch_to_degree
angle_pink.append(temp)#粉球第5个角度
#temp=(math.atan2(table_legth*3.0/4.0,table_half_width)-math.atan2(table_legth/4.0,table_half_width))*ratio_from_arch_to_degree
#angle_pink.append(temp)#粉球第6个角度

angle_pink_middle=[]
temp=(math.atan2(table_half_width,table_legth/4.0)-math.atan2(table_width/4.0,table_legth/4.0))*ratio_from_arch_to_degree
angle_pink_middle.append(temp)#粉球中袋第1个角度
temp=0.0
angle_pink_middle.append(temp)#粉球中袋第2个角度
temp=(math.atan2(table_legth/4.0,table_half_width)-math.atan2(table_legth/4.0-ball_black_distance_top,table_half_width))*ratio_from_arch_to_degree
angle_pink_middle.append(temp)#粉球中袋第3个角度
temp=(math.atan2(table_legth/4.0,table_half_width)-math.atan2(table_legth/4.0-2.0*ball_black_distance_top,table_half_width))*ratio_from_arch_to_degree
angle_pink_middle.append(temp)#粉球中袋第4个角度

angle_blue=[]
temp=math.atan2(table_legth/8.0,table_half_width)*ratio_from_arch_to_degree
angle_blue.append(temp)#篮球中带第一个角度

angle_blue.append(0)#篮球中带第二个角度

temp=math.atan2(table_legth*2.0/8.0-table_break_line_distance_buttom/2.0,table_half_width)*ratio_from_arch_to_degree
angle_blue.append(temp)#篮球中带第三个角度
temp=(math.atan2(table_legth/2.0,table_half_width)-math.atan2(table_legth/2.0-table_break_line_distance_buttom,table_half_width))*ratio_from_arch_to_degree
angle_blue.append(temp)#篮球底带第四个角度
angle_blue.append(0)#篮球底带第五个角度
temp=(math.atan2(table_legth/2.0-table_break_line_distance_buttom,table_ridus_break_cicle)-math.atan2(table_legth/2.0,table_half_width))*ratio_from_arch_to_degree
angle_blue.append(temp)#篮球底带第6个角度

angle_yellow_green=[]
temp=(math.atan2(table_break_line_distance_buttom,table_half_width-table_ridus_break_cicle)-math.atan2(table_legth/2.0-table_break_line_distance_buttom,table_half_width+table_ridus_break_cicle))*ratio_from_arch_to_degree
angle_yellow_green.append(temp)
temp=(math.atan2(table_break_line_distance_buttom,table_half_width-table_ridus_break_cicle)-math.atan2(table_legth/4.0-table_break_line_distance_buttom/2.0,table_half_width+table_ridus_break_cicle))*ratio_from_arch_to_degree
angle_yellow_green.append(temp)

angle_brown=[]
temp=(math.atan2(table_legth/2.0-table_break_line_distance_buttom,table_half_width)-math.atan2(table_break_line_distance_buttom,table_half_width))*ratio_from_arch_to_degree
angle_brown.append(temp)
temp=(math.atan2(table_break_line_distance_buttom,table_half_width)-math.atan2(table_legth/4.0-table_break_line_distance_buttom/2.0,table_half_width))*ratio_from_arch_to_degree
angle_brown.append(temp)
print(my_fix_parameter)
print(my_fix_parameter_quater)
print("黑球瞄准点位分别为:\n角度\t\t位置\t\t修正后位置8\t\t修正后位置4")
for temp in angle_black:
    print(str(round(temp))+'\t\t'+str(round(2.0*math.sin(temp/ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter,ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter_quater,ratio_from_arch_to_degree),2)))
print("\n粉球顶袋瞄准点位分别为:\n角度\t\t位置")
for temp in angle_pink:
        print(str(round(temp))+'\t\t'+str(round(2.0*math.sin(temp/ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter,ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter_quater,ratio_from_arch_to_degree),2)))
print("\n粉球中袋瞄准点位分别为:\n角度\t\t位置")
for temp in angle_pink_middle:
        print(str(round(temp))+'\t\t'+str(round(2.0*math.sin(temp/ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter,ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter_quater,ratio_from_arch_to_degree),2)))
print("\n蓝球瞄准点位分别为:\n角度\t\t位置")
for temp in angle_blue:
        print(str(round(temp))+'\t\t'+str(round(2.0*math.sin(temp/ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter,ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter_quater,ratio_from_arch_to_degree),2)))
print("\n绿球瞄准点位分别为:\n角度\t\t位置")
for temp in angle_yellow_green:
        print(str(round(temp))+'\t\t'+str(round(2.0*math.sin(temp/ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter,ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter_quater,ratio_from_arch_to_degree),2)))
print("\n咖啡球瞄准点位分别为:\n角度\t\t位置")
for temp in angle_brown:
        print(str(round(temp))+'\t\t'+str(round(2.0*math.sin(temp/ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter,ratio_from_arch_to_degree),2))+'\t\t'+str(round(my_fixed_kappa(temp,my_fix_parameter_quater,ratio_from_arch_to_degree),2)))

