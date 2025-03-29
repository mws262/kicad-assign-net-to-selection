import pcbnew
import wx

class AssignNetToSelectionPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Assign Net to Selection"
        self.category = "Modify"
        self.description = "Assign selected items to a chosen net"

    def Run(self):
        board = pcbnew.GetBoard()
        nets_by_name = board.GetNetsByName()
        netnames = sorted([str(n.GetNetname()) for n in nets_by_name.values()])

        parent = wx.FindWindowByName("Pcbnew")
        dialog = wx.SingleChoiceDialog(parent, "Select a net to assign to selection:",
                                       "Assign Net", netnames)

        if dialog.ShowModal() == wx.ID_OK:
            chosen_net = dialog.GetStringSelection()
            netcode = nets_by_name[chosen_net].GetNetCode()

            # Selected pads in footprints
            for fp in board.GetFootprints():
                if fp.IsSelected():
                    for pad in fp.Pads():
                        pad.SetNetCode(netcode)

            # Selected tracks/vias
            for item in board.GetTracks():
                if item.IsSelected():
                    item.SetNetCode(netcode)

            # Graphical items (e.g. lines/arcs) on copper layers
            for drawing in board.GetDrawings():
                if drawing.IsSelected():
                    layer_id = drawing.GetLayer()
                    if board.GetLayerName(layer_id).endswith(".Cu"):
                        if hasattr(drawing, "SetNetCode"):
                            drawing.SetNetCode(netcode)

            pcbnew.Refresh()

        dialog.Destroy()

AssignNetToSelectionPlugin().register()

