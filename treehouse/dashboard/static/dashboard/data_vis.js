function run_data_vis(persons){
    var $ = go.GraphObject.make;

    myDiagram =
      $(go.Diagram, "myDiagramDiv", // the ID of the DIV HTML element
        {
          initialContentAlignment: go.Spot.Center,
          layout: $(go.LayeredDigraphLayout),
          "undoManager.isEnabled": true
        });

     myDiagram.nodeTemplate =
      $(go.Node, "Horizontal",
        { background: "#44CCFF" },
      $(go.TextBlock, "Default Text",
          { margin: 12, stroke: "white", font: "bold 16px sans-serif" },
          new go.Binding("text", "name"))
      );

    // define the Link template
    myDiagram.linkTemplate =
      $(go.Link,
        {      // links cannot be selected by the user
          // curve: go.Link.Bezier,
          layerName: "Background",
            routing: go.Link.Orthogonal,  // may be either Orthogonal or AvoidsNodes
            curve: go.Link.JumpOver// don't cross in front of any nodes
        },
        $(go.Shape,  // this shape only shows when it isHighlighted
          { isPanelMain: true, stroke: null, strokeWidth: 5 },
          new go.Binding("stroke", "isHighlighted", function(h) { return h ? "red" : null; }).ofObject()),
        $(go.Shape,
          // mark each Shape to get the link geometry with isPanelMain: true
          { isPanelMain: true, stroke: "black", strokeWidth: 1 },
          new go.Binding("stroke", "color")),
        $(go.Shape, { toArrow: "Standard" })
      );

    var persons_obj = {};

    for(var i=0; i<persons.length; i++){
        var cur = persons[i];
        var name = cur.name;
        persons_obj[name] = cur;
    }

    var node_list = [];
    var edge_list = [];

    for(var i=0; i<persons.length; i++){
        var cur = persons[i];

        node_list.push({key: cur.id, name: cur.name});

        if(persons_obj[cur.big]) edge_list.push({from: cur.id,  to: persons_obj[cur.big].id, color:"black" });
        if(persons_obj[cur.big_2]) edge_list.push({from: cur.id, to: persons_obj[cur.big_2].id, color:"black" });
        if(persons_obj[cur.assistant_big]) edge_list.push({from: cur.id, to: persons_obj[cur.assistant_big].id, color:"red" });
        if(persons_obj[cur.assistant_big_2]) edge_list.push({from: cur.id, to: persons_obj[cur.assistant_big_2].id, color:"red" });

    }

    // create a few nodes and links
    myDiagram.model = new go.GraphLinksModel(node_list, edge_list);
}


function run_data_vis_big(persons){
    var $ = go.GraphObject.make;
    var myDiagram =
      $(go.Diagram, "myDiagramDiv",
        {
          initialContentAlignment: go.Spot.Center, // center Diagram contents
          "undoManager.isEnabled": true, // enable Ctrl-Z to undo and Ctrl-Y to redo
          layout: $(go.TreeLayout, // specify a Diagram.layout that arranges trees
                    { angle: 90, layerSpacing: 35 })
        });

    // the template we defined earlier
    myDiagram.nodeTemplate =
      $(go.Node, "Horizontal",
        { background: "#44CCFF" },
        $(go.TextBlock, "Default Text",
          { margin: 12, stroke: "white", font: "bold 16px sans-serif" },
          new go.Binding("text", "name"))
      );

    var model = $(go.TreeModel);

    var persons_obj = {};

    for(var i=0; i<persons.length; i++){
        var cur = persons[i];
        var name = cur.name;
        persons_obj[name] = cur;
    }

    var node_list = [];
    var edge_list = [];

    for(var i=0; i<persons.length; i++){
        var cur = persons[i];


        if(persons_obj[cur.big]) node_list.push({key: cur.id, name: cur.name, parent: persons_obj[cur.big].id});

    }
    model.nodeDataArray = node_list;

    myDiagram.model = model;
}

// function run_data_vis2(persons){
//
//     var node_list = [];
//     var edge_list = [];
//
//     var persons_obj = {}
//
//     for(var i=0; i<persons.length; i++){
//         var cur = persons[i];
//         var name = cur.name;
//         persons_obj[name] = cur;
//     }
//
//
//     for(var i=0; i<persons.length; i++){
//         var cur = persons[i];
//
//         node_list.push({id: cur.id, label: cur.name});
//
//         if(persons_obj[cur.big]) edge_list.push({from: cur.id,  to: persons_obj[cur.big].id, color:{color:'red'} , arrows:'to'});
//         if(persons_obj[cur.big_2]) edge_list.push({from: cur.id, to: persons_obj[cur.big_2].id, color:{color:'red'} , arrows:'to'});
//         if(persons_obj[cur.assistant_big]) edge_list.push({from: cur.id, to: persons_obj[cur.assistant_big].id, color:{color:'yellow'} , arrows:'to'});
//         if(persons_obj[cur.assistant_big_2]) edge_list.push({from: cur.id, to: persons_obj[cur.assistant_big_2].id, color:{color:'yellow'} , arrows:'to'});
//
//     }
//
//     console.log(node_list);
//     console.log(edge_list);
//
//
//     // create an array with nodes
//     var nodes = new vis.DataSet(node_list);
//
//       // create an array with edges
//     var edges = new vis.DataSet(edge_list);
//
//       // create a network
//     var container = document.getElementById('mynetwork');
//     var data = {
//         nodes: nodes,
//         edges: edges
//     };
//     var options = {layout:{
//         improvedLayout: false
//         }};
//     var network = new vis.Network(container, data, options);
// }
