#Đánh giá điểm cuối kỳ của một học viên cao học về một môn học nào đó (cao, trung bình, BHấp) căn cứ vào số buổi học (đầy đủ, trung bình, quá ít), năng lực (khá giỏi, trung bình, yếu) và chức vụ (cao, bình BHường, BHấp)
import numpy as np
import skfuzzy as fz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt


X = np.arange(0, 10.1, 0.1)

### Xác định tiền đề và kết luận
BH = ctrl.Antecedent(X, "Buổi học")
NL = ctrl.Antecedent(X, "Năng lực")
CV = ctrl.Antecedent(X, "Chức vụ")
DG = ctrl.Consequent(X, "Đánh giá điểm")


BH["Đầy đủ"] = fz.trapmf(BH.universe, [7.5, 9, 10, 10])
BH["Trung bình"] = fz.trimf(BH.universe, [4, 6, 7.5])
BH["Quá ít"] = fz.trimf(BH.universe, [0, 0, 4.5])

BH.view()

NL["Khá giỏi"] = fz.trapmf(NL.universe, [7.5, 9, 10, 10])
NL["Trung bình"] = fz.trimf(NL.universe, [4, 6, 7.5])
NL["Yếu"] = fz.trimf(NL.universe, [0, 0, 4.5])

NL.view()

CV["Cao"] = fz.trapmf(CV.universe, [7.5, 9, 10, 10])
CV["Bình thường"] = fz.trimf(CV.universe, [4, 6, 7.5])
CV["Thấp"] = fz.trimf(CV.universe, [0, 0, 4.5])

CV.view()

DG["Cao"] = fz.trapmf(DG.universe, [7, 8.5, 10, 10])
DG["Trung bình"] = fz.trapmf(DG.universe, [3.5, 4, 6, 6.5])
DG["Thấp"] = fz.trapmf(DG.universe, [0, 0, 3, 4])

DG.view()

### Các luật liên quan
R1 = ctrl.Rule(BH["Đầy đủ"] & NL["Khá giỏi"] & CV["Cao"], DG["Cao"])
R2 = ctrl.Rule(BH["Đầy đủ"] & NL["Khá giỏi"] & CV["Bình thường"], DG["Cao"])
R3 = ctrl.Rule(BH["Đầy đủ"] & NL["Khá giỏi"] & CV["Thấp"], DG["Trung bình"])

R4 = ctrl.Rule(BH["Đầy đủ"] & NL["Trung bình"] & CV["Cao"], DG["Cao"])
R5 = ctrl.Rule(BH["Đầy đủ"] & NL["Trung bình"] & CV["Bình thường"], DG["Trung bình"])
R6 = ctrl.Rule(BH["Đầy đủ"] & NL["Trung bình"] & CV["Thấp"], DG["Trung bình"])

R7 = ctrl.Rule(BH["Đầy đủ"] & NL["Yếu"] & CV["Cao"], DG["Trung bình"])
R8 = ctrl.Rule(BH["Đầy đủ"] & NL["Yếu"] & CV["Bình thường"], DG["Trung bình"])
R9 = ctrl.Rule(BH["Đầy đủ"] & NL["Yếu"] & CV["Thấp"], DG["Thấp"])

R10 = ctrl.Rule(BH["Trung bình"] & NL["Khá giỏi"] & CV["Cao"], DG["Cao"])
R11 = ctrl.Rule(BH["Trung bình"] & NL["Khá giỏi"] & CV["Bình thường"], DG["Trung bình"])
R12 = ctrl.Rule(BH["Trung bình"] & NL["Khá giỏi"] & CV["Thấp"], DG["Trung bình"])

R13 = ctrl.Rule(BH["Trung bình"] & NL["Trung bình"] & CV["Cao"], DG["Trung bình"])
R14 = ctrl.Rule(BH["Trung bình"] & NL["Trung bình"] & CV["Bình thường"], DG["Trung bình"])
R15 = ctrl.Rule(BH["Trung bình"] & NL["Trung bình"] & CV["Thấp"], DG["Thấp"])

R16 = ctrl.Rule(BH["Trung bình"] & NL["Yếu"] & CV["Cao"], DG["Trung bình"])
R17 = ctrl.Rule(BH["Trung bình"] & NL["Yếu"] & CV["Bình thường"], DG["Trung bình"])
R18 = ctrl.Rule(BH["Trung bình"] & NL["Yếu"] & CV["Thấp"], DG["Thấp"])

R19 = ctrl.Rule(BH["Quá ít"] & NL["Khá giỏi"] & CV["Cao"], DG["Trung bình"])
R20 = ctrl.Rule(BH["Quá ít"] & NL["Khá giỏi"] & CV["Bình thường"], DG["Trung bình"]%.8)
R21 = ctrl.Rule(BH["Quá ít"] & NL["Khá giỏi"] & CV["Thấp"], DG["Trung bình"])

R22 = ctrl.Rule(BH["Quá ít"] & NL["Trung bình"] & CV["Cao"], DG["Trung bình"])
R23 = ctrl.Rule(BH["Quá ít"] & NL["Trung bình"] & CV["Bình thường"], DG["Trung bình"])
R24 = ctrl.Rule(BH["Quá ít"] & NL["Trung bình"] & CV["Thấp"], DG["Thấp"])

R25 = ctrl.Rule(BH["Quá ít"] & NL["Yếu"] & CV["Cao"], DG["Trung bình"])
R26 = ctrl.Rule(BH["Quá ít"] & NL["Yếu"] & CV["Bình thường"], DG["Thấp"])
R27 = ctrl.Rule(BH["Quá ít"] & NL["Yếu"] & CV["Thấp"], DG["Thấp"])


Rules = [R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26,R27]

### Tạo mô hình đề suy diễn

model = ctrl.ControlSystemSimulation(ctrl.ControlSystem(Rules))

### Đưa dữ liệu vào để xử lý
DBH = float(input("Nhập số buổi học (1-10): "))
DNL = float(input("Nhập điểm Năng lực (1-10): "))
DCV = float(input("Nhập mức độ chức vụ (1-10): "))

model.input["Buổi học"] = DBH
model.input["Năng lực"] = DNL
model.input["Chức vụ"] = DCV

model.compute()

### Xuất kết quả
DDG = model.output["Đánh giá điểm"]
print("Khả năng xét điểm là: %.1f" %DDG)


