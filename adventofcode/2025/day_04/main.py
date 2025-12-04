import numpy as np

LIMIT = 4

def get_neighbouts_matrix(mat_bool):
    mat_int = mat_bool.astype(int)
    mat_adj = mat_int.copy()
    ### T: Top  C: Center, B: Bottom
    ### L: Left, C: Center, R: Right
    mat_adj[1:  ,1:  ] += mat_int[ :-1, :-1] # TL
    mat_adj[1:  , :  ] += mat_int[ :-1, :  ] # TC
    mat_adj[1:  , :-1] += mat_int[ :-1,1:  ] # TR
    mat_adj[ :  ,1:  ] += mat_int[ :  , :-1] # CL
    mat_adj[ :  , :-1] += mat_int[ :  ,1:  ] # CR
    mat_adj[ :-1,1:  ] += mat_int[1:  , :-1] # BL
    mat_adj[ :-1, :  ] += mat_int[1:  , :  ] # BC
    mat_adj[ :-1, :-1] += mat_int[1:  ,1:  ] # BR
    mat_adj[~mat_bool] = 0 # trim out artifacts
    return mat_adj

def get_mask_availables(mat_bool):
    mat_adj = get_neighbouts_matrix(mat_bool)
    return np.logical_and(mat_adj > 0, mat_adj < LIMIT + 1) # +1 to take into account that every cell counts itself as a neighbour too

with open("input.txt", 'r') as file:
    data = file.read().strip().split()


mat_chars = np.array([tuple(row) for row in data])
mat_paper_bool = mat_chars == '@'
mat_paper_bool_orig = mat_paper_bool.copy()

count = 0
nremoved = -1
while nremoved != 0:
    mask = get_mask_availables(mat_paper_bool)
    mat_paper_bool &= ~mask
    nremoved = np.sum(mask)
    count += nremoved

print(np.sum(get_mask_availables(mat_paper_bool_orig))) # PART 1: 1508
print(count) # PART 2: 8538

# import prismatui as pr
# class TUI(pr.Terminal):
#     def on_start(self):
#         pr.init_pair(1, pr.COLOR_BLACK, pr.COLOR_CYAN)
#         self.canvas = self.root.create_layer()
#         self.data  = mat_chars
#         self.attrs = np.zeros_like(mat_chars, dtype = int)
#         self.attrs[get_mask_availables(mat_paper_bool_orig)] = pr.get_color_pair(1)
#
#     def on_update(self):
#         self.canvas.draw_matrix('t','l',self.data,self.attrs)
#
#     def should_stop(self):
#         return self.key == pr.KEY_F1
#
# tui = TUI()
# tui.run(fps = 0)
