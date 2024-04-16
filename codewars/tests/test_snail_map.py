from training.codewars.snail_sort import snail
import pytest


@pytest.mark.parametrize("snail_map, expected", [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
                                                 ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                                                 ([[]], []),
                                                 ([[1]], [1]),
                                                 ([[1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 6, 7, 8, 9, 14, 19, 18, 17, 16, 11, 12, 13]],
                                                  [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]),
                                                 ([[275, 932, 630, 421, 51, 236, 989, 269, 624, 486, 158, 313, 585, 361, 527, 316, 151, 869, 88, 911, 42, 156, 846, 79, 394, 974, 170, 835, 820, 826, 421, 661, 64, 146, 291, 316, 672, 240, 498, 59, 464, 538, 603, 314, 465, 575, 848, 229, 978, 79, 52, 449, 745, 341, 164, 261, 547, 572, 413, 609, 379, 968, 518, 529, 593, 353, 799, 550, 933, 146, 376, 360, 654, 573, 186, 513, 874, 301, 914, 152, 995, 121, 119, 992, 539, 115, 949, 793, 518, 432, 982, 404, 779, 865, 17, 830, 384, 885, 791, 401, 76, 745, 319, 896, 891, 828, 802, 188, 608, 13, 910, 41, 402, 602, 730, 842, 680, 39, 834, 299, 345, 37, 504, 946, 88, 265, 438, 937, 326, 657, 943, 170, 798, 390, 182, 12, 556, 246, 30, 454, 553, 789, 955, 842, 608, 526, 175, 725, 828, 386, 712, 956, 257, 699, 561, 251, 891, 957, 968, 224, 55, 258, 878, 359, 631, 805, 248, 354, 905, 229, 642, 519, 452, 622, 752, 16, 836, 557, 377, 300, 491, 858, 218, 647, 198, 507, 274, 310, 246, 836, 91, 61, 737, 230, 71, 622, 539, 70, 407, 466, 488, 631, 170, 156, 603, 506, 149, 927, 821, 912, 742, 604, 379, 474, 202, 785, 57, 923, 713, 681, 828, 135, 264, 921, 926, 260, 337, 751, 215, 625, 149, 702, 554, 533, 749, 749, 185, 799, 741, 705, 654, 301, 134, 747, 633, 617, 388, 942, 690, 665, 167, 372, 721, 546, 491, 905, 856, 225, 735, 69, 412, 88, 580, 253, 14, 395, 923, 220, 260, 151, 255, 711, 788, 123, 351, 844, 143, 857, 338, 700, 263, 46, 694, 366, 885, 836, 41, 37, 932, 470, 162, 263, 104, 714, 382, 727, 598, 519, 581, 212, 476, 752, 262, 104, 926, 553, 818, 512, 405, 146, 977, 772, 961, 371, 824, 630, 796, 995, 44, 1, 594, 416, 106, 818, 969, 732, 805, 891, 431, 350, 793, 365, 688, 467, 403, 210, 742, 657, 579, 817, 419, 774, 321, 569, 349, 825, 341, 411, 236, 66, 738, 707, 271, 179, 443, 963, 137, 956, 395, 229, 546, 102, 77, 789, 292, 976, 762, 24, 766, 75, 2, 209, 105, 231, 89, 942, 796, 367, 898, 877, 665, 127, 573, 109, 353, 172, 841, 74, 526, 109, 415, 345, 749, 631, 75, 645, 280, 700, 58, 137]], [275, 932, 630, 421, 51, 236, 989, 269, 624, 486, 158, 313, 585, 361, 527, 316, 151, 869, 88, 911, 42, 156, 846, 79, 394, 974, 170, 835, 820, 826, 421, 661, 64, 146, 291, 316, 672, 240, 498, 59, 464, 538, 603, 314, 465, 575, 848, 229, 978, 79, 52, 449, 745, 341, 164, 261, 547, 572, 41, 258, 927, 665, 37, 416, 707, 367, 137, 898, 271, 106, 932, 167, 821, 878, 402, 413, 609, 379, 968, 518, 529, 593, 353, 799, 550, 933, 146, 376, 360, 654, 573, 186, 513, 874, 301, 914, 152, 995, 121, 119, 992, 539, 115, 949, 793, 518, 432, 982, 404, 779, 865, 17, 830, 384, 885, 791, 401, 76, 745, 319, 896, 891, 828, 802, 188, 608, 13, 910, 55, 149, 690, 41, 594, 738, 796, 58, 877, 179, 818, 470, 372, 912, 359, 602, 730, 842, 680, 39, 834, 299, 345, 37, 504, 946, 88, 265, 438, 937, 326, 657, 943, 170, 798, 390, 182, 12, 556, 246, 30, 454, 553, 789, 955, 842, 608, 526, 175, 725, 828, 386, 712, 956, 257, 699, 561, 251, 891, 957, 968, 224, 506, 942, 836, 1, 66, 942, 700, 665, 443, 969, 162, 721, 742, 631, 805, 248, 354, 905, 229, 642, 519, 452, 622, 752, 16, 836, 557, 377, 300, 491, 858, 218, 647, 198, 507, 274, 310, 246, 836, 91, 61, 737, 230, 71, 622, 539, 70, 407, 466, 488, 631, 170, 156, 603, 388, 885, 44, 236, 89, 280, 127, 963, 732, 263, 546, 604, 379, 474, 202, 785, 57, 923, 713, 681, 828, 135, 264, 921, 926, 260, 337, 751, 215, 625, 149, 702, 554, 533, 749, 749, 185, 799, 741, 705, 654, 301, 134, 747, 633, 617, 366, 995, 411, 231, 645, 573, 137, 805, 104, 491, 905, 856, 225, 735, 69, 412, 88, 580, 253, 14, 395, 923, 220, 260, 151, 255, 711, 788, 123, 351, 844, 143, 857, 338, 700, 263, 46, 694, 796, 341, 105, 75, 109, 956, 891, 714, 382, 727, 598, 519, 581, 212, 476, 752, 262, 104, 926, 553, 818, 512, 405, 146, 977, 772, 961, 371, 824, 630, 825, 209, 631, 353, 395, 431, 350, 793, 365, 688, 467, 403, 210, 742, 657, 579, 817, 419, 774, 321, 569, 349, 2, 749, 172, 229, 546, 102, 77, 789, 292, 976, 762, 24, 766, 75, 345, 841, 74, 526, 109, 415])])
def test_snail_sort(snail_map, expected):
    assert snail(snail_map) == expected
