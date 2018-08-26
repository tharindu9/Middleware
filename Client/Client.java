import middleware.Middleware;
class Client{
    public static void main(String[] args){
        Middleware mware = new Middleware();
        
        try{
            System.out.println(mware.subService(args[0],args[1],args[2]));
        }catch(Exception e){
            System.out.println(e.getMassege());
        }
    }
}
