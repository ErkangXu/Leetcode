/**
 * #define NEIGHBORS_MAX_SIZE 100
 * struct UndirectedGraphNode {
 *     int label;
 *     struct UndirectedGraphNode *neighbors[NEIGHBORS_MAX_SIZE];
 *     int neighborsCount;
 * };
 */
struct UndirectedGraphNode *cloneGraphHelper(struct UndirectedGraphNode *graph, struct UndirectedGraphNode **cl){
    struct UndirectedGraphNode *result=malloc(sizeof(struct UndirectedGraphNode));
    cl[graph->label+2000]=result; // Though trial and error, I know the range of the label is -2000 ~ 4000
    result->label=graph->label;
    result->neighborsCount=graph->neighborsCount;
    for(int i=0;i<graph->neighborsCount;i++){
        int id = graph->neighbors[i]->label;
        if(cl[id+2000]==NULL) { // The node hasn't been visited, need to create it
            result->neighbors[i]=cloneGraphHelper(graph->neighbors[i], cl);
        } else result->neighbors[i]=cl[id+2000]; // Node already exists, just build the connection to it
    }
    return result;
}

struct UndirectedGraphNode *cloneGraph(struct UndirectedGraphNode *graph) {
    if(!graph) return NULL;
    struct UndirectedGraphNode **checkList=calloc(6000,sizeof(struct UndirectedGraphNode*)); // Should be pointer to the pointer, all NULL
    return cloneGraphHelper(graph,checkList);
}